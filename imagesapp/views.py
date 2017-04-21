from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from models import Image, Rate, Comment
from forms import ImageForm, RateForm, CommentForm


class ImageDetail(DetailView):
    model = Image
    template_name = 'image_detail.html'

    def get_content_data(self, **kwargs):
        context = super(ImageDetail, self).get_context_data(**kwargs)
        return context

class ImageCreate(CreateView):
    model = Image
    template_name = 'form.html'
    form_class = ImageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ImageCreate, self).form_valid(form)

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
