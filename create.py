import sqlite3
conn = sqlite3.connect('test.db')
print("Succesfully Connected")

conn.execute("""
CREATE TABLE TEACHERS(
ID integer primary key not null,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL
)
"""
)
print("Sucessfully created teachers table")
conn.close()