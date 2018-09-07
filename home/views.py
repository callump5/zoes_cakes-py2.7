# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.

def get_home(request):
    category = Category.objects.all()
    return render(request, 'home/home.html', {'category': category})



def get_cakes_in_categorys(request, pk):

    cakes = Item.objects.filter(category=pk)

    return render(request, 'categorys/items.html', {'cakes': cakes})
