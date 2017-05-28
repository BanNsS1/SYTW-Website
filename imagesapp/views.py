from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from models import Image, Rate, Comment
from forms import ImageForm, RateForm, CommentForm
from serializers import ImageSerializer, RateSerializer, CommentSerializer

class APIImageList(generics.ListCreateAPIView):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class APIImageDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class APIRateList(generics.ListCreateAPIView):
    model = Rate
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class APIRateDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Rate
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class APICommentsList(generics.ListCreateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class APICommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LoginRequired(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)

class OwnerRequired(object):
    def get_object(self, *args, **kwargs):
        obj = super(OwnerRequired, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

# USERS

class Register(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def form_valid(self,form):
        new_user = form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                )
        login(self.request, new_user)
        return HttpResponseRedirect("/accounts/profile/")

class UserDetail(DetailView):
    model = User
    template_name = 'user_detail.html'

    def get_content_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        return context

def SelfUserProfile(request):
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, "user_detail.html", {})
    else:
        return HttpResponseRedirect("/accounts/login/")

#IMAGES

def AjaxImageSearch(request):
    q = request.GET.get('q')
    if q is not None:
        results = Image.objects.filter(
            Q(title__contains=q) |
            Q(description__contains = q)).order_by('title')

        data = serializers.serialize('json', results)
        return HttpResponse(data, content_type="application/json")

class ImageDetail(DetailView):
    model = Image
    template_name = 'image_detail.html'

    def get_content_data(self, **kwargs):
        context = super(ImageDetail, self).get_context_data(**kwargs)
        return context

class ImageCreate(LoginRequired, CreateView):
    model = Image
    template_name = 'form.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ImageCreate, self).form_valid(form)

class ImageEdit(LoginRequired, OwnerRequired, UpdateView):
	model = Image
	template_name = 'form.html'
	form_class = ImageForm

	def get_success_url(self):
		return reverse_lazy('imagesapp:image_detail', args=(self.object.id,))

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ImageEdit, self).form_valid(form)

class ImageDelete(LoginRequired, OwnerRequired, DeleteView):
    template_name = 'delete_form.html'

#RATES

class RateDetail(DetailView):
    model = Rate
    template_name = 'rate_detail.html'

    def get_content_data(self, **kwargs):
        context = super(RateDetail, self).get_context_data(**kwargs)
        return context

class RateCreate(LoginRequired, CreateView):
    model = Rate
    template_name = 'form.html'
    form_class = RateForm

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.image.id,))

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.image = Image.objects.get(id=self.kwargs['pk'])

        #Not allowing user to rate more than once the same image.
        rates = Rate.objects.filter(
            Q(image=form.instance.image) &
            Q(user=form.instance.user)
        )
        if len(rates) == 0:
            return super(RateCreate, self).form_valid(form)
        else:
            return HttpResponseRedirect("/imagesapp/images/"+str(form.instance.image.id)+"/?action=rate&error=1")

class RateEdit(LoginRequired, OwnerRequired, UpdateView):
    model = Rate
    template_name = 'form.html'
    form_class = RateForm

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.image.id,))

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(RateEdit, self).form_valid(form)

class RateDelete(LoginRequired, OwnerRequired, DeleteView):
    model = Rate
    template_name = 'delete_form.html'

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.image.id,))

#COMMENTS

class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment_detail.html'

    def get_content_data(self, **kwargs):
        context = super(CommentDetail, self).get_content_data(**kwargs)
        return context

class CommentCreate(LoginRequired, CreateView):
    model = Comment
    template_name = 'form.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.image.id,))

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.image = Image.objects.get(id=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

class CommentEdit(LoginRequired, OwnerRequired, UpdateView):
    model = Comment
    template_name = 'form.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.image.id,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CommentEdit, self).form_valid(form)

class CommentDelete(LoginRequired, OwnerRequired, DeleteView):
    model = Comment
    template_name = 'delete_form.html'

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.image.id,))
