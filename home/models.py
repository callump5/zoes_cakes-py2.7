# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from upload_to_aws import upload_img

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_img, null='True')

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='itemCategory')
    description = models.TextField()
    image = models.ImageField(upload_to=upload_img, null='True')


    def __unicode__(self):
        return self.name
