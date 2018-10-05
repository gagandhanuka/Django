from django.shortcuts import render,redirect
from  employee.DBConnection import addEmp 
from employee.emp_1 import employee1
from django.http import HttpResponse
from .models import employees
from django.template import RequestContext
# Create your views here.
def home2(request):
     return render(request,'employee/home.html',{})
def insertemp(request):
    return render(request, 'employee/insemp.html', {})
def updateemp(request):
    return render(request,'employee/upemp.html',{})
def deleteemp(request):
    return render(request,'employee/delemp.html',{})
def showemp(request):
    emp=[]
    obj=employee1()
    res=obj.showEmp()
    for r in res:
        obj1=employee1()
        obj1.ecode=r[0]
        obj1.ename=r[1]
        obj1.basic=r[2]
        obj1.calc()
        emp.append([obj1.ecode,obj1.ename,obj1.basic,obj1.hra,obj1.da,obj1.ta,obj1.gross_sal,obj1.it,obj1.pf,obj1.net_sal])
    #del obj
    return render(request,'employee/showemp.html',{"emp":emp})
def searchemp(request):
    return render(request,'employee/searchemp.html',{})
def insert_emp(request):
     if (request.method =="POST"):
        empid = request.POST['empid']
        ename = request.POST['ename']
        basic = request.POST['basic']
        
        obj1=employee1()
        obj1.addEmp(empid,ename,basic)
        #emp=employees.objects.all()
        #output=','.join([q.ename for q in emp])
        #return HttpResponse(output)
     #return render(request,'employee/insert',{})
     return redirect('insert')

def delete_emp(request):
    if (request.method =="POST"):
        empid = request.POST['empid']
        obj=employee1()
        obj.deleteEmp(empid)
        #del obj
    #return render(request,'employee/delete',{})
    return redirect('delete')
def update_emp(request):
    if (request.method =="POST"):
        empid = request.POST['empid']
        ename = request.POST['ename']
        basic = request.POST['basic']
        obj=employee1()
        obj.updateEmp(empid,ename,basic)
        #del obj
    #return render(request,'employee/home.hml',{})
    return redirect('update')
def savedata(request):
    if (request.method =="POST"):
        empid = request.POST['empid']
    emp=[]
    str1=""
    obj=employee1()
    res=obj.search(empid)
    for r in res:
        obj1=employee1()
        obj1.ecode=r[0]
        obj1.ename=r[1]
        obj1.basic=r[2]
        obj1.calc()
        emp.append([obj1.ecode,obj1.ename,obj1.basic,obj1.hra,obj1.da,obj1.ta,obj1.gross_sal,obj1.it,obj1.pf,obj1.net_sal])
    for i in emp:
        str1=str1+"<tr>"
        for j in i:
            str1=str1+"<td>"+str(j)+"</td>"
        str1=str1+"</tr>"
    if (res==[]):
        return HttpResponse("No such record Exist")
    return HttpResponse("<table class='table table-hover ' border='2' style='border-collapse: collapse'>"+
            "<tr class='table-info'><th>Employee id</th>"+
            "<th>Employee Name</th>"+
            "<th>Basic Salary</th>"+
            "<th>HRA</th>"+
            "<th>DA</th>"+
            "<th>TA</th>"+
            "<th>Gross Salary</th>"+
            "<th>IT</th>"+
            "<th>PF</th>"+
            "<th>Net Salary</th></tr>"+
            str1+"</table>")