# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from blog.models import Blog
from django.shortcuts import render_to_response

def index(request):
    blog_list=Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})
