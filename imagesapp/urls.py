"""imagesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Image, Rate, Comment
from views import ImageDetail, ImageCreate, RateCreate, CommentCreate
from forms import ImageForm, RateForm, CommentForm


urlpatterns = [
    # List newest 10 images: /imagesapp/
    url(r'^$',
        ListView.as_view(
            queryset=Image.objects.filter(date__lte=timezone.now()).order_by('date')[:10],
            context_object_name='latest_images_list',
            template_name='images_newest.html'
        ),
        name='image_list'
    ),

    # List top rated 10 images: /imagesapp/
    #url(r'^toprated/$',)
    # List most commented 10 images: /imagesapp/
    #url(r'^mostcommented/$',)


# IMAGES
    # View Image /imagesapp/images/1/
    url(r'^images/(?P<pk>\d+)/$',
        ImageDetail.as_view(),
        name = 'image_detail'
    ),

    # Upload Image /imagesapp/images/create
    url(r'^images/create/$',
        ImageCreate.as_view(),
        name='image_create'
    ),

    # Edit image /imagesapp/images/1/edit
    url(r'^images/(?P<pkr>\d+)/edit/$',
        UpdateView.as_view(
            model = Image,
            template_name = 'form.html',
            form_class = ImageForm
        ),
        name='image_edit'
    ),

    # Delete image /imagesapp/images/1/delete
    #url(r'^images/(?P<pkr>\d+)/delete/$')

# RATES
    # View Rate /imagesapp/images/1/rates/1/
    url(r'^rates/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Rate,
            template_name = 'rate_detail.html'
        ),
        name = 'rate_detail'
    ),

    # Rate image /imagesapp/images/1/rates/create
    url(r'^images/(?P<pk>\d+)/rates/create',
        RateCreate.as_view(),
        name='rate_create'
    ),

    # Edit Rate /imagesapp/images/1/rates/edit
    url(r'^rates/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Rate,
            template_name = 'form.html',
            form_class = RateForm
        ),
        name='rate_edit'
    ),

    #Since deleting a rate makes no sense we're not going to provide this feature
    # Delete Rate /imagesapp/images/1/delete
    #url(r'^images/(?P<pk>\d+)/rates/(?P<pk>\d+)/delete/$', )

# COMMENTS
    # View Comment /imagesapp/images/1/comments/1/
    url(r'^comments/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Comment,
            template_name = 'comment_detail.html'
        ),
        name = 'comment_detail'
    ),

    # Comment image /imagesapp/comments/create
    url(r'^images/(?P<pk>\d+)/comments/create',
        CommentCreate.as_view(),
        name='comment_create'
    ),

    # Edit Comment /imagesapp/images/1/comments/1/edit
    url(r'^comments/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Comment,
            template_name = 'form.html',
            form_class = CommentForm
        ),
        name='comment_edit'
    )

    # Delete Comment /imagesapp/images/1/comments/1/delete
    #url(r'^images/(?P<pk>\d+)/comments/(?P<pk>\d+)/delete/$', )
]
