# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin

class Blog(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Blog,BlogAdmin)