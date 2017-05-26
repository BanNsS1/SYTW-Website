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
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from models import Image, Rate, Comment

from views import AjaxImageSearch, ImageDetail, ImageCreate, ImageEdit, ImageDelete
from views import RateCreate, RateEdit, RateDelete
from views import CommentCreate, CommentEdit, CommentDelete

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

    # Search Results /imagesapp/images/search/?q=<NameToSearch>
    url(r'^images/search/$',
        AjaxImageSearch,
        name = 'image_search'
    ),

	#url(r'^toprated/$'),
	#url(r'^mostcommented/$'),

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
    url(r'^images/(?P<pk>\d+)/edit/$',
        ImageEdit.as_view(),
        name='image_edit'
    ),

    # Delete image /imagesapp/images/1/delete
    url(r'^images/(?P<pk>\d+)/delete/$',
        ImageDelete.as_view(
            model = Image,
            success_url = reverse_lazy('imagesapp:image_list')
        ),
        name = 'image_delete'
    ),

# RATES
    # Rate image /imagesapp/images/1/rates/create
    url(r'^images/(?P<pk>\d+)/rates/create',
        RateCreate.as_view(),
        name='rate_create'
    ),

    # Edit Rate /imagesapp/rates/1/edit
    url(r'^rates/(?P<pk>\d+)/edit/$',
        RateEdit.as_view(),
        name='rate_edit'
    ),

    url(r'^rates/(?P<pk>\d+)/delete/$',
        RateDelete.as_view(),
        name = 'rate_delete'
    ),

# COMMENTS
    # Comment image /imagesapp/images/1/comments/create
    url(r'^images/(?P<pk>\d+)/comments/create',
        CommentCreate.as_view(),
        name='comment_create'
    ),

    # Edit Comment /imagesapp/comments/1/edit
    url(r'^comments/(?P<pk>\d+)/edit/$',
        CommentEdit.as_view(),
        name='comment_edit'
    ),

    # Delete Comment /imagesapp/comments/1/delete
    url(r'^comments/(?P<pk>\d+)/delete/$',
        CommentDelete.as_view(),
        name = 'comment_delete'
    )
]
