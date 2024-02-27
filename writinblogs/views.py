from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from writinblogs.models import BlogPost
from writinblogs.forms import BlogPostForm

def index(request):
    context=BlogPost.objects.all()
    return render(request,'homeblog.html',{'context':context})

def createblog(request):
    form=BlogPostForm()
    if request.method=="POST":
        form=BlogPostForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            body=form.cleaned_data['body']
            b=BlogPost(title=title,body=body)
            b.save()
            return HttpResponseRedirect('../displayblog')
    return render(request,'createblog.html',context={'form':form})

def displayblog(request):
    b=BlogPost.objects.all()
    return render(request,'displayblog.html',{'BlogPost':b})