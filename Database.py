
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
    def Assign(self,Type,id):
        query=""
        if Type=="Storage":
          query= "update employees "+"set StorageAccess = ? "+" WHERE id = ?"
        elif Type=="Printer":
                   query= "update employees "+"set PrinterAccess = ? "+" WHERE id = ?"

        elif Type=="Phone":
                 query= "update employees "+"set PhoneAccess = ? "+" WHERE id = ?"

        print(query)
        try:
                     self.cursor.execute(query,(1,id))
                     self.connection.commit()
        except:
                     print("failed")
                     self.connection.rollback()

    def DeAssign(self,Type,id):
            query=""
            if Type=="Storage":
              query= "update employees "+"set StorageAccess = ? "+" WHERE id = ?"
            elif Type=="Printer":
                       query= "update employees "+"set PrinterAccess = ? "+" WHERE id = ?"

            elif Type=="Phone":
                     query= "update employees "+"set PhoneAccess = ? "+" WHERE id = ?"

            print(query)
            try:
                self.cursor.execute(query,(0,id))
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
            print (person)
    def query(self, query):
        try:

            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

        return self.cursor.fetchall()


    def AssignPrinter(self,id):
         self.Assign("Printer",id)

    def AssignPhone(self,id):
        self.Assign("Phone",id)

    def assignStorage(self,id):
         self.Assign("Storage",id)


    def deAssignPrinter(self,id):
        self.DeAssign("Printer",id)

    def deAssignPhone(self,id):
        self.DeAssign("Phone",id)


    def deAssignStorage(self,id):
        self.DeAssign("Storage",id)

    def __del__(self):
        self.connection.close()



db = Database()








if __name__ == "__main__":
    fire.Fire(Database)





# c.execute("insert into employees(name,email,phonenumber) values('Gh','g_z48@yahoo.com','01022222')")
#
# c.execute("select ID from employees")
