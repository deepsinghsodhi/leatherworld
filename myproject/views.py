#Template pages 

from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from . import models
import time
from django.contrib import messages

#middleware to get session for main app routes
def sessioncheck_midddleware(get_response):
    def middleware(request):
        if request.path=='' or  request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or  request.path=='/login/' or  request.path=='/register/':
            request.session['suname']=None
            request.session ['srole']=None

            response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="GET":
        return render(request,"contact.html",{"output":""})
    else:
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        message=request.POST.get('message')
        p=models.Contact(name=name,number=number,email=email,message=message)
        p.save()
        return render(request,"contact.html",{"output":messages.info(request, 'Your message has sent...')})

def products(request):
    return render(request,"products.html")

def register(request):
    if request.method=="GET":
        return render(request,"register.html",{"output":""})
    else:
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        info=time.asctime()
        p=models.Register(name=name,username=username,password=password,mobile=mobile,address=address,city=city,gender=gender,role='user',status=0,info=info)
        p.save()
        return render(request,"register.html",{"output":messages.info(request, 'User registered Successfully...')})
def login(request):
    if request.method=="GET":
        return render(request,"login.html",{"output":""})
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        userdetails=models.Register.objects.filter(username=username,password=password,status=1)
        
        if len(userdetails)>0:
            request.session['suname']=userdetails[0].username
            request.session['srole']=userdetails[0].role
            request.session['uname']=userdetails[0].name
            if userdetails[0].role=="admin":
                return redirect('/myadmin/')
            else:
                return redirect('/users/')
        else:
            return render(request,"login.html",{"output":messages.info(request, 'Invalid User or Verify Your Account...')})
            

def checkEmail(request):
    emailid=request.GET.get("emailid")
    result=models.Register.objects.filter(username__startswith=emailid).exists()
    if result:
        s=1                  #1 means id exists
    else:
        s=0
    return HttpResponse(s)



