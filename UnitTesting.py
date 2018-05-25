import sqlite3
import unittest
import fire

from Database import Database

class EmployeesTest(unittest.TestCase):



    def test_Insertion(self):
        self.connection =  sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("drop table employees")
        self.Database=Database()
        Success =self.Database.AddEmployee( "Gharam","g_z48@yahoo.com","01022227777")

        self.cursor.execute(""" SELECT * FROM employees""")
        #Since Database is Empty .. Gharam will be first Element

        data=self.cursor.fetchone()
        #Id Should be 1
        self.assertTrue(Success==1)
        self.assertTrue(data[0]==1)
        self.assertTrue(data[1]=="Gharam")
        self.assertTrue(data[2]=="g_z48@yahoo.com")
        self.assertTrue(data[3]=="01022227777")
        self.assertTrue(data[4]==0)
        self.assertTrue(data[5]==0)
        self.assertTrue(data[6]==0)



    def TestInsertionFailure(self):
        self.Database.AddEmployee( "Romy",None,"010222222")
        self.cursor.execute(""" SELECT * FROM employees""")
        data=self.cursor.fetchall()
        #Since Database is Empty .. it should result in 1
        self.assertTrue(len(data)==1)







test= EmployeesTest()

test.test_Insertion()



# Make The CLI using Fire
if __name__ == "__main__":
    unittest.main()
