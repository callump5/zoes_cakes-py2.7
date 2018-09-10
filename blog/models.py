# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    post = models.TextField()
    pub_date = models.DateTimeField(default=timezone.datetime.now())
    image = models.ImageField(blank=False)

    def __unicode__(self):
        return self.title