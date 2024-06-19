import sqlite3
conn = sqlite3.connect('test.db')
print("Successfully connected")

conn.execute("DELETE FROM TEACHERS WHERE ID=6"
)
conn.commit()

data = conn.execute("SELECT * FROM TEACHERS ")
for teachers in data:
    print("ID ;",teachers[0])
    print("FIRSTNAME ;",teachers[1])
    print("LASTNAME;",teachers[2])
    print("AGE ;",teachers[3])
    print("SALARY ;",teachers[4])

print("Successfully DELETED data")
conn.close()