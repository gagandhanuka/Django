#imports
from test1 import conn

con_obj=conn()

def addEmp(empid,ename,basic):
        
        con_obj.empinsert(empid,ename,basic)


'''
def input(self):
        try:
            self.ecode=int(input("Please enter employee code: "))
            self.ename=input("Please enter employee name: ")
            self.basic=int(input("Please enter employee's basic salary: "))
            self.status=1
        except:
            print("Wrong input values")
            self.ecode=0
            self.ename=""
            self.basic=0
def calc(self):
        self.hra=0.4*self.basic
        self.da=0.2*self.basic
        self.ta=0.1*self.basic
        self.gross_sal=self.basic+self.hra+self.da+self.ta
        self.it=0.2*self.gross_sal
        self.pf=0.1*self.gross_sal
        self.net_sal=self.gross_sal-(self.it+self.pf)
def disp(self):
        print("\n")
        print("Employee Id: ",self.ecode)
        print("Employee name: ",self.ename)
        print("Employee's basic: ",self.basic)
        print("Employee's HRA:",self.hra)
        print("Employee's DA:",self.da)
        print("Employee's TA:",self.ta)
        print("Employee's Gross Salary:",self.gross_sal)
        print("Employee's Income Tax",self.it)
        print("Employee's PF",self.pf)
        print("Employee's Net Salary",self.net_sal)
        print("\n\n")
    
def addEmp(self,empid,ename,basic):
        self.ecode=empid
        self.ename=ename
        self.basic=basic
        self.con_obj.empinsert(self.ecode,self.ename,self.basic)

def updateEmp(self,empid,ename,basic):
        try:
            self.ecode=empid
            self.ename=ename
            self.basic=basic
            if(self.con_obj.empupdate(self.ecode,self.ename,self.basic)>0):
                print("Employee updated")
            else:
                print("Employee doesn't exist")
        except:
            print("Wrong input values")
def deleteEmp(self,empid):
        try:
            self.ecode=empid
            if(self.con_obj.empdelete(self.ecode)>0):
                print("Employee deleted")
            else:
                print("Employee doesn't exist")
        except:
            print("Wrong input values")
def showEmp(self):
        flag=0
        res=self.con_obj.empshow()
        return res
def search(self):
        try:
            self.ecode=int(input("Please enter employee code: "))
            res=self.con_obj.empsearch(self.ecode)
            if(self.con_obj.empexist(self.ecode)):
                print("Employee doesn't exist")
            else:
                for r in res:
                    flag=1
                    self.ecode=r[0]
                    self.ename=r[1]
                    self.basic=r[2]
                    self.calc()
                    self.disp()
        except :
            print("Wrong input values")

'''