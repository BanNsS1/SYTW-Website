from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from models import Image, Rate, Comment
from forms import ImageForm, RateForm, CommentForm

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

class ImageDetail(DetailView):
    model = Image
    template_name = 'image_detail.html'

    def get_content_data(self, **kwargs):
        context = super(ImageDetail, self).get_context_data(**kwargs)
        return context

class ImageCreate(LoginRequired,CreateView):
    model = Image
    template_name = 'form.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse_lazy('imagesapp:image_detail', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ImageCreate, self).form_valid(form)

class ImageDelete(LoginRequired, OwnerRequired, DeleteView):
    template_name = 'delete_form.html'


class RateCreate(CreateView):
    model = Rate
    template_name = 'form.html'
    form_class = RateForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.image = Image.objects.get(id=self.kwargs['pk'])
        return super(RateCreate, self).form_valid(form)

class CommentCreate(CreateView):
    model = Comment
    template_name = 'form.html'
    form_class = CommentForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.image = Image.objects.get(id=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

class CommentDelete(LoginRequired, OwnerRequired, DeleteView):
    template_name = 'delete_form.html'
