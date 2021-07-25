from django.shortcuts import render,redirect
from myproject import models as myproject_models
from . import models
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, response
from django.contrib import messages
from django.conf import settings

import time
media_url=settings.MEDIA_URL
# middleware function to check user details at application level 

def sessioncheckmyadmin_midddleware(get_response):
    def middleware(request):
        if request.path=='/myadmin/' or  request.path=='/myadmin/manageusers/' or request.path=='/myadmin/managecategories/' or request.path=='/myadmin/manageproduct/' or request.path=='/myadmin/manageuserstatus/' or request.path=='/myadmin/managesubcategory/':
            if request.session['suname']==None or request.session ['srole']!="admin":
                response= redirect('/login/')
            else:
                response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware

def adminhome(request):
    return render(request,'adminhome.html')

def manageusers(request):
    userdetails=myproject_models.Register.objects.filter(role="user")
    return render(request,'manageusers.html',{"userdetails":userdetails})

def manageuserstatus(request):
    s=request.GET.get("s")
    regid = request.GET.get("regid")
    if s=="block":
        myproject_models.Register.objects.filter(regid=regid).update(status=0)
    elif s=="verify":
        myproject_models.Register.objects.filter(regid=regid).update(status=1)
    else:
        myproject_models.Register.objects.filter(regid=regid).delete()
    return redirect('/myadmin/manageusers/')
    
def managecategories(request):
    if request.method=="GET":
        return render(request,"managecategories.html",{"output":""})
    else:        
        catname=request.POST.get("catname")
        caticon=request.FILES["caticon"]
        fs=FileSystemStorage()
        filename =fs.save(caticon.name,caticon)
        p=models.Category(catname=catname,caticonname=filename)
        p.save()
        return render(request,"managecategories.html",{"output":messages.info(request, 'Category added Successfully...')})

def managesubcategory(request):
    clist=models.Category.objects.all()

    if request.method=="GET":
        return render(request,"managesubcategory.html",{"output":"","clist":clist})
    else:        
        catid=request.POST.get("catid")
        subcatname=request.POST.get("subcatname")
        caticon=request.FILES["caticon"]
        fs=FileSystemStorage()
        filename =fs.save(caticon.name,caticon)
        p=models.Subcategory(catid=catid,subcatname=subcatname,subcaticonname=filename)
        p.save()
        return render(request,"managesubcategory.html",{"output":messages.info(request, 'Sub Category added Successfully...')})

def manageproduct(request):
    clist=models.Category.objects.all()
    if request.method=="GET":
        return render(request,"manageproduct.html",{"clist":clist,"output":""})
    else:
        title=request.POST.get("title")
        catid=request.POST.get("catid")
        subcatid=request.POST.get("subcat id")
        pdescription=request.POST.get("pdescription")
        bprice=request.POST.get("bprice")
        info=time.time()

        piconname=request.FILES["piconname"]
        fs=FileSystemStorage()
        filename =fs.save(piconname.name,piconname)
        
        p=models.Product(title=title,catid=catid,subcatid=subcatid,pdescription=pdescription,bprice=bprice,piconname=filename,info=info)
        p.save()
        return render(request,"manageproduct.html",{"clist":clist,"output":messages.info(request, 'Your Product has been added...')})

def viewproduct(request):
    plist=models.Product.objects.all()
    return render(request,'viewproduct.html',{"plist":plist,"media_url":media_url})


def fetchSubCategory(request):
    catid=request.GET.get('catid')
    sclist=models.Subcategory.objects.filter(catid=int(catid))
    sclist_options="<option>Select Sub Category</option>"
    for row in sclist:
        sclist_options+=("<option value='"+str(row.subcatid)+"'>"+row.subcatname+"</option>")
    return HttpResponse(sclist_options)
    
# Create your views here.
