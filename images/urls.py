"""images URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from imagesapp.views import UserDetail, SelfUserProfile, Register

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imagesapp/', include('imagesapp.urls', namespace='imagesapp')),
    url(r'^accounts/profile/$', SelfUserProfile, name='myprofile'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', UserDetail.as_view(), name='profile'),

    url(r'^accounts/login/$', login, name='login'),

    url(r'^accounts/register/$', Register.as_view(), name='register'),

    url(r'^accounts/logout/$', logout, name='logout')
]
