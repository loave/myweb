# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Question,Choice

# Create your views here.
def index(request):
    latest_question_list=Question.objects.all()
    content={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',content)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=question_id)
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':p,'error_message':"you didn't select a choice",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))