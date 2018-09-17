# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import LandingText, HomeText, AboutPage, ContactDetails
# Register your models here.

admin.site.register(LandingText)
admin.site.register(HomeText)
admin.site.register(AboutPage)
admin.site.register(ContactDetails)
