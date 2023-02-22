import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
query = """CREATE TABLE STUDENT2(ROLLNO INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, 
CLASS INT NOT NULL, ROOM INT NOT NULL)"""
conn.execute(query)
print("Table created successfully")
# Step-2: Inserting into a Table
query = """ INSERT INTO STUDENT2(ROLLNO,NAME,CLASS,ROOM) VALUES (11212506, 'SNEHIT GARG',  'BTECH', 144 ) """
conn.execute(query)
conn.commit()
print("Records created successfully")
# Step-3: Selection/Retrieve data from a Database
cursor = conn.execute("SELECT ROLLNO, name, CLASS, ROOM from STUDENT2")
for row in cursor:
    print("ROLLNO = 11212506 ", row[0])
print("NAME = Snehit garg ", row[1])
print("CLASS = BTECH ", row[2])
print("ROOM = 144 ", row[3])
print("Operation done successfully")
#conn.close()
# Step-4: Deletion from Table:
cursor = conn.execute("DELETE FROM STUDENT2 WHERE ROLLNO = 11212505")
print("Record delete successfully")
conn.close()