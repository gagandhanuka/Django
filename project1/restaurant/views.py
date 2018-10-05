from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from restaurant.testrestaurant import conn1
from restaurant.testlocation import conn2
from django.core.files.storage import FileSystemStorage
import os
import random
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def createrest(request):
    return render(request,"restaurant/restaurant_signup.html",{})
def addrest(request):
    if(request.method=='POST'):
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        phn_no=request.POST["phn_no"]
        owner=request.POST["owner"]
        obj=conn1()
        obj.restinsert(username,email,phn_no,password,owner)
    return HttpResponse("New account created")
def addloc(request):
    return render(request,"restaurant/addloc.html",{}) 
def createloc(request):
    if(request.method=='POST'  ):
        branch_name=request.POST["branch_name"]
        area=request.POST["area"]   
        city=request.POST["city"]
        state=request.POST["state"]
        country=request.POST["country"]
        pin=request.POST["pin"]
        rest_type=request.POST["rest_type"]
        photo=request.FILES.get("myfile","")
        if photo!="":
            img_extension = os.path.splitext(photo.name)[1]
            user_folder = 'img/'
            str1="avatar"+str(random.random())+img_extension
            img_save_path =user_folder+'/'+str1
            with open(img_save_path, 'wb+') as f:
             for chunk in photo.chunks():
                f.write(chunk)
        obj=conn2()
        obj.locinsert(request.session["rid"],branch_name,area,city,state,country,pin,rest_type,str1)
        return redirect("/restaurant/addlocation")
def viewloc(request,rid):
    obj=conn2()
    locations=obj.locshow(rid)
    list1=[]
    if (locations==[]):
        return HttpResponse("No records Exist")
    for e in locations:
        list1.append({"lid":e[1],"branch_name":e[2],"area":e[3],"city":e[4],"state":e[5],"country":e[6],"pin":e[7],"rest_type":e[8],"photo":e[10]})
    return render(request,"restaurant/viewloc.html",{"locations":list1})
@csrf_exempt
def editloc(request,lid):
    obj=conn2()
    location=obj.locsearchbyid(lid)
    list1=[]
    for e in location:
        list1.append({"lid":e[1],"branch_name":e[2],"area":e[3],"city":e[4],"state":e[5],"country":e[6],"pin":e[7],"rest_type":e[8],"photo":e[10]})
    
    return render(request,"restaurant/editloc.html",{"location":list1})

def editloc1(request):
    obj=conn2()
    if request.method=="POST":
        lid=request.POST["lid"]
        branch_name=request.POST["branch_name"]
        area=request.POST["area"]
        city=request.POST["city"]
        state=request.POST["state"]
        country=request.POST["country"]
        pin=request.POST["pin"]
        rest_type=request.POST["rest_type"]
        photo=request.POST["photo"]
        obj.locupdate(lid,branch_name,area,city,state,country,pin,rest_type,photo)
        if photo!="":
            img_extension = os.path.splitext(photo.name)[1]
            user_folder = 'img/'
            str1="avatar"+str(random.random())+img_extension
            img_save_path =user_folder+'/'+str1
            with open(img_save_path, 'wb+') as f:
             for chunk in photo.chunks():
                f.write(chunk)
        return redirect("/restaurant/viewloc/")
    return HttpResponse("Access to this page is denied")
def searchloc(request):
    if request.method=="POST":
        branch_name=request.POST.get("branch_name","@@#$%^%")
        rid=request.session["rid"]
        if branch_name=="":
            return HttpResponse("")
        str1=""
        list1=[]
        obj=conn2()
        locations=obj.locsearchbybranch(rid,branch_name)
        if locations==[]:
            return HttpResponse("No such record Exist")
        for e in locations:
            list1.append({'lid':e[1],"branch_name":e[2],"area":e[3],"city":e[4],"state":e[5],"country":e[6],"pin":e[7],"rest_type":e[8],"photo":e[10]})
        for i in list1:
            str1=str1+"<tr><td>"+str(i["lid"])+"</td><td>"+i["branch_name"]+"</td><td>"+i["area"]+"</td><td>"+i["city"]+"</td>"
            str1=str1+"<td>"+i["state"]+"</td><td>"+i["country"]+"</td><td>"+str(i["pin"])+"</td><td>"+i["rest_type"]+"</td>"
            str1=str1+'<td><img src="http://www.gstatic.com/webp/gallery/1.jpg" width=100px height=100px/>'
            str1=str1+'<img src="file://C:/Users/HP/Envs/project1/restaurant/templates/restaurant/b.jpg" width=100px height=100px/></td>'
            str1=str1+'<td><form action="../editloc/'+str(i["lid"])+'/" method="POST"><div class="container-fluid"><button type="submit" class="btn btn-info ">Edit</button></div></form></td></tr>'
        return HttpResponse('<table class="table table-hover " border="2" style="border-collapse: collapse">' +
            '<tr class="table-info "><th>Location id</th> '+
                '<th>Branch Name</th>'+
                '<th>Area</th>'+
                '<th>City</th>'+
                '<th>State</th>'+
                '<th>Country</th>'+
                '<th>Pin</th>'+ 
                '<th>Type</th>'+
                '<th>Location View</th>'+
                '<th>Edit</th>'+
            '</tr>'+str1+'</table>')
    return HttpResponse("Please enter something valid")
def search(request):
    return render(request,"restaurant/locsearch.html",{})