# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .upload_to_aws import upload_img

from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = HTMLField()
    image = models.ImageField(upload_to=upload_img, null='True')

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='itemCategory', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    description = HTMLField()
    image = models.ImageField(upload_to=upload_img, null='True')


    def __unicode__(self):
        return self.name
