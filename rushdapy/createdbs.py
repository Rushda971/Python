'''
mysql = database software 
python =  controls
xampp = runs the mysql

'''
# To connect install : pip install mysql-connector-python

import mysql.connector

mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",  #
    password =""
)
print("Connected successfully")

''' cursor ek connector hai mysql and python yeh ek pointer function hai'''
mycursor=mydb.cursor()

#create database
mycursor.execute("create database if not exists employees_db")
print("database created")

mycursor.execute("use employees_db")


mycursor.execute('''
     create table if not exists employees (
     id int,
     name varchar(30),
     dep varchar(20),
     role varchar(20),
     city varchar(20)
                 
)''')
print("table created")
 
# ‼ create table topic remaining------------------????

''' %s - placeholder hai(khali jagah) --actual value baad mein aate hai 
koi bhi value aane se pehle like john se pehle %s hota hai

directly koi insert nhi hota hai??--sql injection

'''

#insert