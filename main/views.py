from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def HomePage(request):
    return render(request,"index.html")

def ClientPage(request):
    data=Member.objects.all()
    return render(request,"client.html",{"data1":data})

def LoginPage(request):
    return render(request,"login.html")

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
