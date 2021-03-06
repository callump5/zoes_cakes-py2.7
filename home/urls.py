"""zoe_cakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import get_items, get_cat_items, get_gallery, get_about, get_contact

urlpatterns = [
    url(r'about/$', get_about, name='about'),
    url(r'gallery/$', get_gallery, name='gallery'),
    url(r'contact/$', get_contact, name='contact'),
    url(r'^category/(?P<slug>[-\w]+)/$', get_items, name='category'),
    url(r'^category/item/(?P<pk>\d+)/$', get_cat_items, name='items'),
]