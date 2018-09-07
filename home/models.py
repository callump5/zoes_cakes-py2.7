# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/uploads', null='True')

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    description = models.TextField()
    image = models.ImageField(upload_to='static/uploads', null=True)


    def __unicode__(self):
        return self.name
