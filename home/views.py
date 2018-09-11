# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category, Item
from blog.models import BlogPost
# Create your views here.

def get_home(request):
    category = Category.objects.all()
    posts = BlogPost.objects.all()[0:2]
    return render(request, 'home/home.html', {'category': category,
                                              'posts': posts})


def get_items(request, slug):
    items = Item.objects.filter(category__name__startswith=slug)
    return render(request, 'categorys/items.html', {'items': items})