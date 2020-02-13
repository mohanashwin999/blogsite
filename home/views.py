from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import post
from .forms import *


def signup(req):
    if req.method=='POST':
        new_user=User.objects.create_user(
            username=req.POST.get('username'),
            email=req.POST.get('email'),
            password=req.POST.get('password'),
            first_name=req.POST.get('fname'),
            last_name=req.POST.get('lname'))
        return redirect('home:login')
    else:
        return render(req,'home/signup.html')

def loginUser(req):
    if req.method=='POST':
        user=authenticate(username=req.POST.get('username'),
        password=req.POST.get('password'))
        if user:
            login(req,user)
            return redirect('home:post')
        else:
            return HttpResponse('Invalid credentials or Access Blocked!')
    else:
        return render(req,'home/login.html')

@login_required
def addpost(req):
    if req.method=='POST':
        new_post=post()
        new_post.title=req.POST.get('title')
        new_post.content=req.POST.get('content')
        new_post.posted_by=req.user
        new_post.save()
        return redirect('home:index')
    else:
        return render(req,'home/post.html',{'data':req.user})

@login_required
def logoutUser(req):
    logout(req)
    return redirect('home:login')

def index(req):
    posts=post.objects.all()
    return render(req,'home/index.html',{'posts':posts})

def get_post_by_username(req):
    user=User.objects.get(username=req.GET['name'])
    posts=post.objects.filter(posted_by=user)
    return render(req,'home/index.html',{'posts':posts})

def get_post_by_date(req):
    month=req.GET['month']
    year=req.GET['year']
    print(month,year)
    posts=post.objects.filter(timestamp__month=month,timestamp__year=year)
    return render(req,'home/index.html',{'posts':posts})



def get_post_by_year(req):
    year=req.GET['year']
    posts=post.objects.filter(timestamp__year=year)
    return render(req,'home/index.html',{'posts':posts})

def get_id(req,key):
    posts=post.objects.filter(id=key)
    return render(req,'home/index.html',{'posts':posts})

def contactus(req):
    if req.method=='POST':
        form=ContactForm(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print(name,email,message)
            return HttpResponse('success')
    else:
        form=ContactForm()    
        return render(req,'home/contactus.html',{'data':req.user,'form':form})