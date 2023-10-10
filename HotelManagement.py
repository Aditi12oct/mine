# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 07:24:32 2022

@author: hp
"""

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
if mycon.is_connected()==False:
    print('error connecting to mysql database')
cursor=mycon.cursor()
cursor.execute("select*from customer1")
data=cursor.fetchall()
count=cursor.rowcount
for customerID in data:
    print(customerID)
    
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
if mycon.is_connected()==False:
    print('error connecting to mysql database')
cursor=mycon.cursor()
cursor.execute("select*from customer1")
data=cursor.fetchone()
count=cursor.rowcount
print ("total number of rows retrived from customer1:",count)
print (data)

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
if mycon.is_connected()==False:
    print('error connecting to mysql database')
cursor=mycon.cursor()
cursor.execute("select*from customer1")
data=cursor.fetchmany(3)
count=cursor.rowcount
print ("total number of rows retrived from customer1:",count)
print (data)


import mysql.connector as sqltor 
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
if mycon.is_connected()==False:
   print('error connecting to mysql database')
cursor=mycon.cursor()
cursor.execute("select*from bookings0")
data=cursor.fetchall()
count=cursor.rowcount
for customerID in data:
    print(customerID)


import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
if mycon.is_connected()==False:
    print('error connecting to mysql database')
cursor=mycon.cursor()
cursor.execute("select*from rooms1")
data=cursor.fetchall()
count=cursor.rowcount
for roomno in data:
    print(roomno)
    
    
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
if mycon.is_connected()==False:
   print('error connecting to mysql database')
cursor=mycon.cursor()
def menu():
 print("WELCOME TO PURPLE ORCHID:")
 print("Menu:-")
 print("1.customer1")
 print("2.rooms1")
 print("3.bookings0")
 print("4.exit")
 ch=int(input("Enter your choice(1-3):"))
 if (ch==1):
       sql="select*from customer1"
       cursor.execute(sql)
       data=cursor.fetchall()
       for customerID in data:
           print(customerID)
 elif (ch==2):
       sql1="select*from rooms1"
       cursor.execute(sql1)
       data=cursor.fetchall()
       for roomno in data:
           print(roomno)
 elif (ch==3):
       sql2="select*from bookings0"
       cursor.execute(sql2)
       data=cursor.fetchall()
       for customerID in data:
           print(customerID)
 else:
       print("exit")
menu()
 
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
cursor=mycon.cursor()

def customer1():
    print("do u want to register:Enter 4 if yes")
    ch=int(input("enter your choice:"))
    if (ch==4):
        customerID=input('enter customerID:')
        firstname=input('enter firstname:')
        surname=input('enter surname:')
        phoneno=input('enter phoneno:')
        adharno=input('enter adharno:')
        city=input('enter city:')
        roomno=input('enter roomnno:')
        total_bill=input('enter total_bill:')
        sq="insert into customer1(customerID,firstname,surname,phoneno,adharno,city,roomno,total_bill)values({},'{}','{}',{},{},'{}',{},{})".format(customerID,firstname,surname,phoneno,adharno,city,roomno,total_bill)
        cursor.execute(sq)
        mycon.commit()
customer1()

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
cursor=mycon.cursor()

def rooms1():
    print("do u want to see the rooom type avalable: enter 5 if yes")
    ch=int(input("enter your choice:"))
    if (ch==5):
        q="select*from rooms1"
        cursor.execute(q)
        data=cursor.fetchall()
        for roomtype in data:
            print(roomtype)
rooms1()
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root123",database="Hotel_Management")
cursor=mycon.cursor()

def bookings1():
    print("do u want to book a room:enter 6 if yes")
    ch=int(input("enter your choice:"))
    if (ch==6):
       customerID=input('enter customerID:')
       roomno=input('enter the roomno u selected:')
       arrival=input('enter the arrival date:')
       departure=input('enter the departure date:')
       totalstay=input('enter the no. of days you will stay:')
       totalpay=input('enter the amount :')
       t="insert into bookings1(customerID,roomno,arrival,departure,totalstay,totalpay)values({},{},{},{},{},{})".format(customerID,roomno,arrival,departure,totalstay,totalpay)
       cursor.execute(t)
       mycon.commit()
bookings1()

print("thanks for visiting")


     




    
    
    
    