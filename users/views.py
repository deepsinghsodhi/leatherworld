from myproject.settings import MEDIA_URL
from django.shortcuts import redirect, render
from django.conf import settings

from myadmin import models as myadmin_models
from myproject import models as myproject_models
from . import models
from django.contrib import messages

import time
from math import ceil
media_url=settings.MEDIA_URL

def userhome(request):
    print(request.session['suname'])
    return render(request,'userhome.html',{"uname":request.session['uname'],"suname":request.session['suname']})

def vdeals(request):
    clist=myadmin_models.Category.objects.all()
    return render(request,'vdeals.html',{"clist":clist,"media_url":media_url,"suname":request.session['suname']})

def vscdeals(request):
    catid=request.GET.get("catid")
    sclist=myadmin_models.Subcategory.objects.filter(catid=int(catid))
    return render(request,'vscdeals.html',{"sclist":sclist,"media_url":media_url,"suname":request.session['suname']})

def vpdeals(request):
    subcatid=request.GET.get("subcatid")
    plist=myadmin_models.Product.objects.filter(subcatid=int(subcatid))
    scname=myadmin_models.Subcategory.objects.filter(subcatid=int(subcatid))
    ptime=myadmin_models.Product.objects.filter(pid=int(subcatid))
    allProds=[]
    n=len(plist)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([plist, range(1, nSlides), nSlides])
    # params={'allProds':allProds }
    for row in plist:
        if (time.time()-float(row.info))>172800:
            bstatus=0
        else:
            bstatus=1
        print(bstatus)
    return render(request,'vpdeals.html',{"ptime":ptime,"scname":scname[0],"bstatus":bstatus,"plist":plist,"media_url":media_url,'allProds':allProds ,"suname":request.session['suname']})



def productview(request,myid):
    paypalURL="https://www.sandbox.paypal.com/cgi-bin/webscr"
    paypalID="sb-sayvp6851368@business.example.com"
    # //sb-247neq6858778@personal.example.com
    product=myadmin_models.Product.objects.filter(pid=myid)
    return render(request,"productview.html",{"paypalURL":paypalURL,"paypalID":paypalID,'product':product,"media_url":media_url})
# def bitproduct(request):
#     if request.method=="GET":
#         pid=int(request.GET.get("pid"))
#         pdetails=myadmin_models.Product.objects.filter(pid=int(pid))
#         bdetails=models.Bidding.objects.filter(productid=int(pid))
#             if len(bdetails)>0:
#                 cbprice=bdetails[0].bidprice
#                 for row in bdetails:
#                     if row.bidprice>cbprice:
#                     cbprice=row.bidprice
#             else:
#                 cbprice=pdetails[0].bprice

#         if (time.time()-float(pdetails[0].info))>172800:
#             bstatus=0
#         # print("Sale ends")
#         else:
#             bstatus=1
#         # print("Sale is live now")
#         return render(request,'bitproduct.html',{"bstatus":bstatus,"pdetails":pdetails[0],"media_url":media_url,"cbprice":cbprice,"suname":request.session['suname']})
#     else:
#         p=models.Bidding(productid=request.post.get('pid'),uid=request.post.get('uid'),productid=request.post.get('bidprice'),info=time.asc())
#         p.save()
#         return redirect("/users/bidproduct/?")
   
def cpuser(request):
    if request.method=="GET":
        return render(request,"cpuser.html",{"suname":request.session['suname']})
    else:
        opass=request.POST.get("opass")
        npass=request.POST.get("npass")
        cnpass=request.POST.get("cnpass")
        userdetails=myproject_models.Register.objects.filter(username=request.session['suname'],password=opass)
        print(npass)
        print(userdetails)
        if len(userdetails)>0:
            if npass==cnpass:
                myproject_models.Register.objects.filter(username=request.session['suname']).update(password=cnpass)
                msg="password changed sucessfully"
            else:
                msg="New and confirm passoword mismatch,try again"
        else:
            msg="Incorrect old password"
        return render(request,"cpuser.html",{"suname":request.session['suname'],"output":messages.info(request,msg)})

def epuser(request):
    userdetails=myproject_models.Register.objects.filter(username=request.session['suname'])
    m,f="",""
    if userdetails[0].gender=="male":
        m="checked"
    else:
        f="checked"
    if request.method=="GET":
        return render(request,"epuser.html",{"suname":request.session['suname'],"userdetails":userdetails[0],"m":m,"f":f})
    else:
        name=request.POST.get('name')
        username=request.POST.get('username')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        p=myproject_models.Register.objects.filter(username=username).update(name=name,username=username,mobile=mobile,address=address,city=city,gender=gender)
        return redirect("/users/epuser/")
        # return render(request,"register.html",{"output":messages.info(request, 'User registered Successfully...')})