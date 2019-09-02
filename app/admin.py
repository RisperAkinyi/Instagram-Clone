# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profiles,Images,Comments
from django.contrib import admin

# Register your model class here.
admin.site.register(Profiles)
admin.site.register(Images)
admin.site.register(Comments)