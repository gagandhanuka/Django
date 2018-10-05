import mysql.connector
class conn:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',password='123456', database='hrms',host='localhost')
        self.cursor =self.cnx.cursor()        
    def adminexist(self,username,password):
        str1="select *from web_portal_admin where status=1 and username='"+username+"' and password='"+password+"'" 
        self.cursor.execute(str1)
        res = self.cursor.fetchall()
        for r in res:
            return False
        return True