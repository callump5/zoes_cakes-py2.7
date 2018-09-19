# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tinymce.models import HTMLField


# Create your models here.

class CategoryHeader(models.Model):
    text = HTMLField()

    def __unicode__(self):
        return 'Category Header'

class LandingText(models.Model):
    text = HTMLField()

    def __unicode__(self):
        return 'Landing Text'

class HomeText(models.Model):
    text = HTMLField()

    def __unicode__(self):
        return 'Home Text'

class AboutPage(models.Model):
    text = HTMLField()

    def __unicode__(self):
        return 'About Page'

class ContactDetails(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Contact Details'
