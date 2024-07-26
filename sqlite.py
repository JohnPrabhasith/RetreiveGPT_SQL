import sqlite3

#Connect ot SQLite database
connection = sqlite3.connect("Student.db")

#create a cursor to inserting record data,create table
cursor = connection.cursor()

#Create Table
table_info ="""
CREATE TABLE Student(Name varchar(30),Class varchar(10),
Section varchar(10),Marks int);
"""

cursor.execute(table_info)

#insert The records
cursor.execute("""
Insert into student values('BLJP','DataScience', 'A', 98);
""")
cursor.execute("""
Insert into student values('John','MachineLearning', 'B', 85);
""")
cursor.execute("""
Insert into student values('Raju','WebDev', 'A', 21);
""")
cursor.execute("""
Insert into student values('Ram','DevOps', 'D', 56);
""")
cursor.execute("""
Insert into student values('Nazeer','AeroSpace', 'A', 52);
""")
cursor.execute("""
Insert into student values('Kaira','QuantumScience', 'C', 90);
""")


print("Record Inserted Successfully")
data = cursor.execute("Select * from Student")

for r in data:
    print(r)

#commit the connection
connection.commit()
connection.close()