from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def HomePage(request):
    if str(request.user)=='AnonymousUser':
        client="Gost"
        email=""
    else:
        client=request.user
        email=request.user.email
    data=[{"img":"iphone5.jpg","text":"Apple iPhone 15 Pro (128 GB) - Blue Titanium : Amazon.co.uk: Everything Else"}]
    return render(request,"index.html",{"client":client,"email":email,"data":data})


def LoginPage(request):
    if request.method=="POST":
        if 'login' in request.POST:
            email=request.POST.get("e")
            password=request.POST.get("p")
            
            a=authenticate(username=email,password=password)
            print(a)
            print("True")
            if a is not None:
                login(request,a)
                return redirect("/")
            else:
                return redirect("/login/")
        if 'signin' in request.POST:
            username=request.POST.get("un")
            email=request.POST.get("e")
            password1=request.POST.get("p1")
            password2=request.POST.get("p2")
            if password1==password2:
                a=User.objects.create_user(username,email,password1)
                login(request,a)
                return redirect("/")
            else:
                return redirect("/signin/")
    return render(request,"login.html")

def LogoutPage(request):
    logout(request)
    return redirect("/")

def SigninPage(request):
    return render(request,"signin.html")


def AddMailPage(request,firstname,lastname,age,phone,cmail,password,male):
    member=Member(firstname=firstname,lastname=lastname,age=age,phone=phone,cmail=cmail,password=password,male=male)
    member.save()
    data=Member.objects.all()
    return render(request,"client.html",{"data1":data})
    

def MailPage(request,cmail,password):
    datas=Member.objects.all()
    for i in datas:
        print(i)
        if i.password==password and i.cmail==cmail:
            i["error"]="none"
            data={"error":"error","cmail":"","password":"","phone":"","firstname":"","lastname":"","age":""}
            break
    else:
        data={"error":"error","cmail":"","password":"","phone":"","firstname":"","lastname":"","age":""}
    return render(request,"cmail.html",{"data1":data})


# Create your views here.
