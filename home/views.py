# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category, Item
# Create your views here.

def get_home(request):
    category = Category.objects.all()
    return render(request, 'home/home.html', {'category': category})

def get_items(request, slug):
    items = Item.objects.filter(category__slug__contains=slug)
    category = Category.objects.get(slug__exact=slug)
    return render(request, 'home/category_items.html', {'items': items,
                                                        'category': category})
