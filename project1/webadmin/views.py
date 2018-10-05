from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from webadmin.web_admin import conn
from webadmin.testrestaurant import conn1
from restaurant.testlocation import conn2
def login(request):
    request.session['username']=""
    request.session['password']=""
    request.session['login_type']=""
    return render(request,'webadmin/login.html',{"message":""})
def test(request):
    return render(request,'webadmin/test.html',{})
def check(request):
    if(request.method=="POST"):
        username=request.POST["user"]
        password=request.POST["pass"]
        login_type=request.POST["radio"]
        obj=conn()
        obj1=conn1()
        if(obj.adminexist(username,password) and login_type=="Admin"):
            return render(request,'webadmin/login.html',{"message":"The credits you filled were wrong "})
        if(obj1.restexist(username,password)==0 and login_type=="Restaurant"):
            return render(request,'webadmin/login.html',{"message":"The credits you filled were wrong "})
        request.session['username']=username
        request.session['password']=password
        request.session['login_type']=login_type
        if login_type=="Admin":
            return redirect("/adminhome")
        request.session['rid']=obj1.restexist(username,password)
    return render(request,"restaurant/restauranthome.html",{"rid":request.session['rid']})
def search(request):
    username=request.session['username']
    password=request.session['password']
    login_type=request.session['login_type']
    if(username==""):
        return render(request,'webadmin/login.html',{"message":""})
    if(login_type!="Admin"):
        return HttpResponse("Acess to this page is denied")
    return render(request,"webadmin/searchrestaurant.html",{})
def searchbyuser(request):
    username=request.session['username']
    password=request.session['password']
    login_type=request.session['login_type']
    if(username==""):
        return render(request,'webadmin/login.html',{"message":""})
    if(login_type!="Admin"):
        return HttpResponse("Acess to this page is denied")
    return render(request,"webadmin/searchbyusername.html",{})
def adminhome(request):
    username=request.session['username']
    password=request.session['password']
    login_type=request.session['login_type']
    if(username==""):
        return render(request,'webadmin/login.html',{"message":""})
    if(login_type!="Admin"):
        return HttpResponse("Acess to this page is denied")
    return render(request,'webadmin/adminhome.html',{})
def show_to_admin(request):
    username=request.session['username']
    password=request.session['password']
    login_type=request.session['login_type']
    if(username==""):
        return render(request,'webadmin/login.html',{"message":""})
    if(login_type!="Admin"):
        return HttpResponse("Acess to this page is denied")
    obj=conn1()
    list1=[]
    restaurants=obj.restshow()
    if (restaurants==[]):
        return HttpResponse("No records Exist")
    for e in restaurants:
        list1.append({"Rid":e[0],"username":e[1],"email":e[2],"phn_no":e[3],"password":e[4],"verified":e[5],"owner":e[7]})
    return render(request,"webadmin/showrestaurant.html",{"restaurants":list1})
def search_rest(request):
    if(request.method=="POST"):
        rid=request.POST.get("Rid",0)
    obj=conn1()
    str1=""
    list1=[]
    restaurants=obj.restsearchbyid(rid)
    if (restaurants==[]):
        return HttpResponse("No such record Exist")
    for e in restaurants:
        list1.append([e[0],e[1],e[2],e[3],e[4],e[5],e[7]])
    for restaurant in list1:
        str1=str1+"<tr>"
        str1=str1+"<td>"+str(restaurant[0])+"</td>"
        str1=str1+"<td>"+str(restaurant[1])+"</td>"
        str1=str1+"<td>"+str(restaurant[2])+"</td>"
        str1=str1+"<td>"+str(restaurant[3])+"</td>"
        str1=str1+"<td>"+str(restaurant[4])+"</td>"
        if(restaurant[5]==1):
            str1=str1+"<td class='text-success'>Verified</td>"
        else:
            str1=str1+"<td class='text-Danger'>Not Verified</td>"
        str1=str1+"<td>"+restaurant[6]+"</td>"
        if(restaurant[5]==1):
            str1=str1+"<td>Already Verified</td>"
        else:
            str1=str1+"<td><form action='/checked/"+str(restaurant[0])+"'><button class='btn btn-success'>Verify</td>"
        str1=str1+"<td align='center'><form action='/viewloc/"+str(restaurant[0])+"'><button class='btn btn-info' style='width:80%;height:60%'>View</td></tr>"
    return HttpResponse("<table class='table table-hover ' border='2' style='border-collapse: collapse'>"+
            "<tr class='table-info'><th>Restaurant id</th>"+
            "<th>Username</th>"+
            "<th>Email</th>"+
            "<th>Phone no.</th>"+
            "<th>Password</th>"+
            "<th>Verified</th>"+
            "<th>Owner</th><th>Verify</th><th>View</th></tr>"+
            str1+"</table>")
def checkit(request,Rid):
    obj=conn1()
    obj.restverify(Rid,request.session['username'])
    return redirect("/search")
def search_restbyname(request):
    if(request.method=="POST"):
        rname=request.POST.get("rname","@$#%@$")
    if rname=="":
        rname="@$#%@$"
    obj=conn1()
    str1=""
    list1=[]
    restaurants=obj.restsearchbyuser(rname)
    if (restaurants==[]):
        return HttpResponse("No such record Exist")
    for e in restaurants:
        list1.append([e[0],e[1],e[2],e[3],e[4],e[5],e[7]])
    for restaurant in list1:
        str1=str1+"<tr>"
        str1=str1+"<td>"+str(restaurant[0])+"</td>"
        str1=str1+"<td>"+str(restaurant[1])+"</td>"
        str1=str1+"<td>"+str(restaurant[2])+"</td>"
        str1=str1+"<td>"+str(restaurant[3])+"</td>"
        str1=str1+"<td>"+str(restaurant[4])+"</td>"
        if(restaurant[5]==1):
            str1=str1+"<td class='text-success'>Verified</td>"
        else:
            str1=str1+"<td class='text-Danger'>Not Verified</td>"
        str1=str1+"<td>"+restaurant[6]+"</td>"
        if(restaurant[5]==1):
            str1=str1+"<td>Already Verified</td>"
        else:
            str1=str1+"<td><form action='/checked/"+str(restaurant[0])+"'><button class='btn btn-success'>Verify</td>"
        str1=str1+"<td align='center'><form action='/viewloc/"+str(restaurant[0])+"'><button class='btn btn-info' style='width:80%;height:60%'>View</button></form></td></tr>"
    return HttpResponse("<table class='table table-hover ' border='2' style='border-collapse: collapse'>"+
            "<tr class='table-info'><th>Restaurant id</th>"+
            "<th>Username</th>"+
            "<th>Email</th>"+
            "<th>Phone no.</th>"+
            "<th>Password</th>"+
            "<th>Verified</th>"+
            "<th>Owner</th><th>Verify</th><th>View</th></tr>"+
            str1+"</table>")
def viewloc(request,rid):
    obj=conn2()
    locations=obj.locshow(rid)
    list1=[]
    if (locations==[]):
        return HttpResponse("No records Exist")
    for e in locations:
        list1.append({"lid":e[1],"branch_name":e[2],"area":e[3],"city":e[4],"state":e[5],"country":e[6],"pin":e[7],"rest_type":e[8],"photo":e[10]})
    return render(request,"webadmin/viewloc.html",{"locations":list1})
