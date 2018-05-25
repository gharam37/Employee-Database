
import sqlite3
import fire


class Database:


    def __init__(self):
        self.connection =conn = sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
            ID INTEGER  PRIMARY KEY AUTOINCREMENT ,
            name varchar(50) ,
            email varchar(50),
            phonenumber varchar(10),
            PhoneAccess bit,
            PrinterAccess bit,
            StorageAccess bit
            )""")


    def insert(self,query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            print("failed")
            self.connection.rollback()

    def add(self, name,email,phonenumber):

        b="insert into employees(name,email,phonenumber)values("

        comma="'"
        query =b+comma+name+comma+","+comma+email+comma+","+comma+phonenumber+comma+")"



        try:

            print(query);

            self.cursor.execute(query)
            self.connection.commit()
        except:
            print("failed")
            self.connection.rollback()


    def run(self):
        select_query = """
            SELECT * FROM employees
            """
        people = db.query(select_query)
        for person in people:
            print ("There %s " % person[1])
    def query(self, query):
        try:

            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()

db = Database()

# del_query = "DELETE FROM employees"
# db.insert(del_query)

# Data Insert into the table
# query ="""insert into employees(name,email,phonenumber)
# values('Romy','g_z48@yahoo.com','01022222')"""

# # db.query(query)
# db.insert(query)




# Data retrieved from the table

# def run(self):
#     select_query = """
#         SELECT * FROM employees
#         """
#     people = db.query(select_query)
#     for person in people:
#         return ("Found %s " % person[1])


if __name__ == "__main__":
    fire.Fire(Database)





# c.execute("insert into employees(name,email,phonenumber) values('Gh','g_z48@yahoo.com','01022222')")
#
# c.execute("select ID from employees")
