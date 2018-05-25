
import sqlite3
import fire
from Paginator import Paginator
class Database:

    #Intialize the class .. Create table if it doesn't exist
    def __init__(self):
        self.connection =conn = sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
            ID INTEGER  PRIMARY KEY AUTOINCREMENT ,
            name varchar(50) NOT NULL,
            email varchar(50) NOT NULL,
            phonenumber varchar(10) NOT NULL,
            PhoneAccess bit Default 0,
            PrinterAccess bit Default 0,
            StorageAccess bit Default 0
            )""")
        self.Paginator=Paginator()

    #Called by Smaller methods To Assign permissions based on type and id
    def Assign(self,Type,id):
        query=""
        if Type=="Storage":
          query= "update employees "+"set StorageAccess = ? "+" WHERE id = ?"
        elif Type=="Printer":
                   query= "update employees "+"set PrinterAccess = ? "+" WHERE id = ?"

        elif Type=="Phone":
                 query= "update employees "+"set PhoneAccess = ? "+" WHERE id = ?"

        self.Paginator.Paginate()
        try:
                     self.cursor.execute(query,(1,id))
                     self.connection.commit()
                     return 1
        except:
                     print("failed")
                     self.connection.rollback()
                     return 0
    # Remove a permission given an ID
    def DeAssign(self,Type,id):
            query=""
            if Type=="Storage":
              query= "update employees "+"set StorageAccess = ? "+" WHERE id = ?"
            elif Type=="Printer":
                       query= "update employees "+"set PrinterAccess = ? "+" WHERE id = ?"

            elif Type=="Phone":
                     query= "update employees "+"set PhoneAccess = ? "+" WHERE id = ?"

            self.Paginator.Paginate()
            try:
                self.cursor.execute(query,(0,id))
                self.connection.commit()
            except:
                print("failed")
                self.connection.rollback()




    # Given attributes .. insert into Database the following values
    def AddEmployee(self, name,email,phonenumber):

        b="insert into employees(name,email,phonenumber)values("

        comma="'"
        query =b+comma+name+comma+","+comma+email+comma+","+comma+phonenumber+comma+")"



        try:

            self.cursor.execute(query)
            self.connection.commit()
            self.Paginator.Paginate()
            return 1
        except:
            print("failed")
            return 0
            self.connection.rollback()
    #List everything in Paginator
    def ListAll(self):
        self.Paginator.ListAll()
   #List a specific page in Paginator
    def ListOne(self,number):
        self.Paginator.ListOne(number)



    # Call general method Assign and give it a type and an ID
    def AssignPrinter(self,id):
         self.Assign("Printer",id)

    def AssignPhone(self,id):
        self.Assign("Phone",id)

    def assignStorage(self,id):
         self.Assign("Storage",id)

    # Call general method Assign and give it a type and an ID
    def deAssignPrinter(self,id):
        self.DeAssign("Printer",id)

    def deAssignPhone(self,id):
        self.DeAssign("Phone",id)


    def deAssignStorage(self,id):
        self.DeAssign("Storage",id)

    def __del__(self):
        self.connection.close()




# Make The CLI using Fire
if __name__ == "__main__":
    fire.Fire(Database)
