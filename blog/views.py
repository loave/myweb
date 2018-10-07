# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Blog
from django.shortcuts import render_to_response
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib import  auth
# Create your views here.


def index(request):
    blog_list=Blog.objects.all()
    # return render_to_response('index.html',{'blogs':blog_list})
    return render(request, 'index.html', {'blogs': blog_list})

def login(request):
    blog_list=Blog.objects.all()
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    users_=[username]
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)    #验证登录
    # if username !=''and password!='':
        response=HttpResponseRedirect('/login_ok/')
        # response.set_cookie('username',username,1200) #cookie
        request.session['username']=users_    #session
        return response
    else:
        return render(request,'index.html',{'error':'username or passwd error','blogs':blog_list})

def login_ok(request):
    blog_list = Blog.objects.all()
    # username = request.COOKIES.get('username', '')  #cookie
    username=request.session.get('username','') #session
    user=username[0]
    return render(request,'login_ok.html',{'user':username,'blogs':blog_list})
    # if username=='zl' and password=='jamesraul':
    #     return HttpResponse('login success!')
    #
    # else:
    #     # return render_to_response('index.html', {'error': 'username or password error!','blogs':blog_list})
    #     return  render(request,'index.html',{'error':'username or password error!','blogs':blog_list})


# return render_to_response('index.html',{'error':'username or password error!'})
# pdf中的写法是这样写的，但是在1.11.15版本的django中如果这样写的话，会报错不能通过csrf token验证，在网上查了之后，换成这种写法就不会报错，同时还需要在模板views.py里的form表单后边加上{%csrf_token%}；csrf token验证的开关是在settings.py中的中间件middleware部分'django.middleware.csrf.CsrfViewMiddleware'来开启的，把这一行注释掉也能解决这个问题，但这样做必然降低了安全性

def logout(request):
    response=HttpResponseRedirect('/index/')
    # response.delete_cookie('username')  #cookie
    del request.session['username']
    return response

