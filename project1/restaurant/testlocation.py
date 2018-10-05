import mysql.connector
class conn2:
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
    def locinsert(self,rid,branch_name,area,city,state,country,pin,rest_type,photo):
        str1="insert into location(rid,branch_name,area,city,state,country,pin,type,status,photo)values("+str(rid)+",'"+branch_name+"','"+area+"','"+city+"','"+state+"','"+country+"',"+str(pin)+",'"+rest_type+"',1,'"+photo+"')"
        self.cursor.execute(str1)
        self.cnx.commit() 
        str2="update restaurant set verified=0 where rid="+str(rid)
        self.cursor.execute(str2)
        self.cnx.commit() 
    def locupdate(self,lid,branch_name,area,city,state,country,pin,rest_type,photo):
        str2=""
        if(photo==""):
            str2=",photo='"+photo+"'"
        str1="update location set branch_name='"+branch_name+"',area='"+area+"',city='"+city+"',state='"+state+"',country='"+country+"',pin="+str(pin)+",type='"+rest_type+"'"+str2+" where lid="+lid
        self.cursor.execute(str1)
        self.cnx.commit()
        return self.cursor.rowcount
    def locdelete(self,empid):
        str1="update employee set status=0 where eid="+str(empid) 
        self.cursor.execute(str1)   
        self.cnx.commit()
        return self.cursor.rowcount
    def locshow(self,rid):
        str1="select * from location where status=1 and rid="+str(rid) 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        return res
    def locsearchbyid(self,lid):
        str1="select * from location where lid="+str(lid) 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        print(res)
        return res
    def locsearchbybranch(self,rid,branch_name):
        str1="select * from location where rid="+str(rid)+" and branch_name like '"+branch_name+"%'"
        print(str1)
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        print(res)
        return res
#obj=conn2()
#obj.locinsert(3,'subhash restaurant2','New Golden Avenue','Amritsar','Punjab','India',143001,'veg',"C:\\Users\\HP\\Pictures\\Screenshots\\Screenshot (5).png")
#obj.restupdate('subhash restaurant2','subhash1@suhashrest.com',8196923006,'HelloWorld','sudhir')
#obj.restsearchbyuser('s');
