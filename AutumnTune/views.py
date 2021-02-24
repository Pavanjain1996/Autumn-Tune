from django.shortcuts import render, redirect
from .models import UserData, File
from django.db.models import Q
from django.views.generic import ListView

uname = ''
searchtext = ''

def index(request):
    global uname
    if uname != '':
        return render(request,'TuneIn/Home.html',{'username':uname})
    else:
        return redirect('/')

def register(request):
    return render(request,'TuneIn/Register.html')

def registration(request):
    global uname
    first = request.POST['fname']
    middle = request.POST['mname']
    last = request.POST['lname']
    uname = request.POST['username']
    passw = request.POST['password']
    mo = request.POST['mobile']
    xender = request.POST['gender']
    categry = request.POST['category']
    userData = UserData(fname=first,mname=middle,lname=last,username=uname,password=passw,mobile=mo,gender=xender,category=categry)
    userData.save()
    return redirect('/Home')

def login(request):
    return render(request,'TuneIn/Login.html')

def verifylogin(request):
    a=1
    global uname
    uname = request.POST['username']
    passw = request.POST['password']
    data = UserData.objects.all().filter(username=uname)
    for i in data:
        if i.password == passw:
            a=0;
            return redirect('/Home')

    if a == 1:
        return redirect('/')

def profile(request):
    global uname
    if uname != '':
        data = UserData.objects.all().filter(username=uname)
        return render(request,'TuneIn/Profile.html',{'username':uname,'data':data})
    else:
        return redirect('/')
    
def logout(request):
    global uname
    uname = ''
    return redirect('/')

def search(request):
    global seachtext
    searchtext = request.POST['content']
    return redirect('/Answer')
