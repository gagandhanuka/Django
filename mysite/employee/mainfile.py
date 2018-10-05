from emp_1 import employee
#main code
obj=employee()
while True:
    c = int(input('=============================\nPress 1. to add new employee\nPress 2. to update an existing employee\nPress 3.\
to delete existing employee\nPress 4 to show details of an existing employee\nPress 5. search for an employee\nPress 6. to exit') )

    if(c==1):
        obj.addEmp()
    elif(c==2):
        obj.updateEmp()
    elif(c==3):
        obj.deleteEmp()
    elif(c==4):
        obj.showEmp()
    elif(c==5):
        obj.search()
    elif(c==6):
        break
del obj
