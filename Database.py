import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()

# c.execute("drop table employees")


c.execute("""CREATE TABLE employees(
    ID INTEGER  PRIMARY KEY AUTOINCREMENT ,
    name text NOT NULL,
    email text,
    phonenumber varchar(10),
    PhoneAccess bit,
    PrinterAccess bit,
    StorageAccess bit
    )""")


c.execute("insert into employees(name,email,phonenumber) values('Romy','g_z48@yahoo.com','01022222')")

c.execute("select ID from employees")

print(c.fetchall())
print('End for code')
conn.commit()

conn.close()
