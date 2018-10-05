import mysql.connector
class conn1:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',password='123456', database='hrms',host='localhost')
        self.cursor =self.cnx.cursor()        
    def restexist(self,username,password):
        str1="select *from restaurant where username='"+str(username)+"' and password='"+str(password)+"'" 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        for r in res:
            return r[0]
        return 0
    def restinsert(self,username,email,phn_no,password,owner):
        str1="insert into restaurant(username,email,phn_no,password,verified,owner)values('"+username+"','"+email+"',"+str(phn_no)+",'"+password+"',0,'"+owner+"');" 
        self.cursor.execute(str1)
        self.cnx.commit() 
    def restupdate(self,username,email,phn_no,password,owner):
        str1="update restaurant set email='"+email+"',owner='"+owner+"',phn_no="+str(phn_no)+" where username='"+username+"'and password='"+password+"'" 
        self.cursor.execute(str1)
        self.cnx.commit()
        return self.cursor.rowcount
    def empdelete(self,empid):
        str1="update employee set status=0 where eid="+str(empid) 
        self.cursor.execute(str1)   
        self.cnx.commit()
        return self.cursor.rowcount
    def restshow(self):
        str1="select * from restaurant" 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        return res
    def restsearchbyid(self,rid):
        str1="select * from restaurant where rid="+str(rid) 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        return res
    def restsearchbyuser(self,username):
        str1="select * from restaurant where username like '"+username+"%'"
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        return res
    def restverify(self,rid,verified_by):
        str1="update restaurant set verified=1,verified_by='"+ verified_by+"' where rid="+str(rid)
        self.cursor.execute(str1)
        self.cnx.commit()
        return self.cursor.rowcount