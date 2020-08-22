import sqlite3
import re
s=0
conn=sqlite3.connect("Assignment.db")
conn.execute(''' create table if not exists Assignment(name text,email text,mobile text,type char,experience integer,salary integer)''')
while(s<3):
    print("1.Add Employee\n2.Display Employee\n3.Exit")
    s=int(input("Enter your choice::"))
    if(s==1):
        nm=input("Enter name:")
        email=input("Enter Email:")
        mob=input("Enter Mobile no:")
        tp=input("Enter type::")
        exp=int(input("Enter Experience::"))
        epattern=re.compile(r'[\w.-]+@[\w.-]+')
        mpattern=re.compile(r'\d{10}')
        sal=exp*550
        if(epattern.search(email) and mpattern.search(mob)):
            conn.execute("insert into Assignment values(:name,:email,:mob,:type,:exp,:sal)",{'name':nm,'email':email,'mob':mob,'type':tp,'exp':exp,'sal':sal})
            conn.commit()
        else:
            print("Invalid Email and mobile number entered")
    elif(s==2):
        i=int(input("Enter Employee ID::"))
        if(i>0):
            c=conn.execute("select * from Assignment")
            l=c.fetchall()
            print(l[i-1])
            conn.commit()
        else:
            print("Id must be greater than 0")
print("Exited!!")
