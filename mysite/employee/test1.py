import mysql.connector
### insert, udpate, delete
#cursor.execute("insert into employee(eid,ename,sal) values(111,'testuser',444444)")
#cnx.commit()
# read
class conn:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',password='123456', database='hrms',host='localhost')
        self.cursor =self.cnx.cursor()        
    def empexist(self,empid):
        str1="select *from employee where status=1 and eid="+str(empid) 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        for r in res:
            return False
        return True
    def empinsert(self,empid,ename,sal):
        str1="insert into employee(eid,ename,sal,status)values("+str(empid)+",'"+ename+"',"+str(sal)+",1)" 
        self.cursor.execute(str1)
        self.cnx.commit() 
    def empupdate(self,empid,ename,sal):
        str1="update employee set ename='"+ename+"',sal="+str(sal)+" where status=1 and eid="+str(empid) 
        self.cursor.execute(str1)
        self.cnx.commit()
        return self.cursor.rowcount
    def empdelete(self,empid):
        str1="update employee set status=0 where eid="+str(empid) 
        self.cursor.execute(str1)   
        self.cnx.commit()
        return self.cursor.rowcount
    def empshow(self):
        str1="select * from employee where status=1" 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        return res
    def empsearch(self,empid):
        str1="select * from employee where status=1 and eid="+str(empid) 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        return res