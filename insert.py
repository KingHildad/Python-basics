import sqlite3
conn = sqlite3.connect('test.db')
print("Successfully connnected")

conn.execute("INSERT INTO TEACHERS VALUES(1, 'James', 'Kariuki', 45, 56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Enock','Njenga',12,5600.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Raul','Mendez',15,20000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Joy','Jimenes',30,15000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Cindy','Wamatangi',25,86000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Dybala','Kariuki',50,7000.00)")

conn.commit()
print("Sucessfully inserted records")

conn.close()
