# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . models import HomeText, ContactDetails, LandingText, AboutPage, CategoryHeader
from items.models import Category, Item
# Create your views here.

def get_home(request):
    landing_text = LandingText.objects.all()
    home_text = HomeText.objects.all()
    contact = ContactDetails.objects.all()
    cat_header = CategoryHeader.objects.all()
    category = Category.objects.all()
    return render(request, 'home/home.html', {'landing_text':landing_text,
                                              'home_text': home_text,
                                              'contact': contact,
                                              'cat_header': cat_header,
                                              'category': category,})

def get_items(request, slug):
    items = Item.objects.filter(category__slug__contains=slug)
    category = Category.objects.get(slug__exact=slug)
    landing_text = LandingText.objects.all()
    return render(request, 'home/category_items.html', {'items': items,
                                                        'category': category,
                                                        'landing_text':landing_text})
def get_cat_items(request, pk):
    item = Item.objects.get(pk=pk)
    landing_text = LandingText.objects.all()
    return render(request, 'home/item.html', {'item': item,
                                              'landing_text': landing_text})


def get_about(request):
    about = AboutPage.objects.all()
    landing_text = LandingText.objects.all()
    return render(request, 'about/about.html', {'about': about,
                                              'landing_text': landing_text})

def get_gallery(request):
    items = Item.objects.all()
    landing_text = LandingText.objects.all()
    return render(request, 'gallery/gallery.html', {'items': items,
                                              'landing_text': landing_text})

def get_contact(request):
    contact = ContactDetails.objects.all()
    landing_text = LandingText.objects.all()
    return render(request, 'contact/contact.html', {'contact': contact,
                                              'landing_text': landing_text})