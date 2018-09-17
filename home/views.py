# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . models import HomeText, ContactDetails, LandingText, AboutPage
from items.models import Category, Item
# Create your views here.

def get_home(request):
    landing_text = LandingText.objects.get(pk=1)
    home_text = HomeText.objects.get(pk=1)
    contact = ContactDetails.objects.get(pk=1)

    category = Category.objects.all()
    return render(request, 'home/home.html', {'landing_text':landing_text,
                                              'home_text': home_text,
                                              'contact': contact,
                                              'category': category})

def get_items(request, slug):
    items = Item.objects.filter(category__slug__contains=slug)
    category = Category.objects.get(slug__exact=slug)
    return render(request, 'home/category_items.html', {'items': items,
                                                        'category': category})
def get_cat_items(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'home/item.html', {'item': item})