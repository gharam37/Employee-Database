import sqlite3
import unittest
import fire
from Database import Database


class EmployeesTest(unittest.TestCase):

    def test_Insertion(self):
        self.connection = sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("drop table employees")
        self.Database = Database()
        Success = self.Database.AddEmployee("Gharam",
                                            "g_z48@yahoo.com",
                                            "01022227777")

        self.cursor.execute(""" SELECT * FROM employees""")
        # Since Database is Empty .. Gharam will be first Element
        data = self.cursor.fetchone()
        # Id Should be 1
        self.assertTrue(Success == 1)
        self.assertTrue(data[0] == 1)
        self.assertTrue(data[1] == "Gharam")
        self.assertTrue(data[2] == "g_z48@yahoo.com")
        self.assertTrue(data[3] == "01022227777")
        self.assertTrue(data[4] == 0)
        self.assertTrue(data[5] == 0)
        self.assertTrue(data[6] == 0)

    def test_InsertionFailure(self):
            self.connection = sqlite3.connect('employees.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute("drop table employees")
            self.Database = Database()
            Success = self.Database.AddEmployee("Gharam",
                                                "g_z48@yahoo.com",
                                                "010b")
            self.assertTrue(Success == 0)

    #  After u Insert one Element in the Databse .. give it 3 accesses
    def test_AccessSuccess(self):
            self.connection = sqlite3.connect('employees.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute("drop table employees")
            self.Database = Database()
            self.Database.AddEmployee("Gharam",
                                      "g_z48@yahoo.com",
                                      "01022227777")
            Success = self.Database.Assign("Storage", 1)
            self.cursor.execute(""" SELECT StorageAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(Success == 1)
            self.assertTrue(data[0] == 1)   # Storage Access Set to 1

            Success = self.Database.Assign("Printer", 1)
            self.cursor.execute(""" SELECT PrinterAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(Success == 1)
            self.assertTrue(data[0] == 1)  # Printer Access Set to 1

            Success = self.Database.Assign("Phone", 1)
            self.cursor.execute(""" SELECT PhoneAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(Success == 1)
            self.assertTrue(data[0] == 1)  # Phone Access Set to 1

    def test_deAccSuccess(self):
            self.connection = sqlite3.connect('employees.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute("drop table employees")
            self.Database = Database()
            self.Database.AddEmployee("Gharam", "g_z48@yahoo.com", "010222277")

            self.Database.Assign("Storage", 1)
            self.cursor.execute(""" SELECT StorageAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(data[0] == 1)  # Set it to One First
            Success = self.Database.DeAssign("Storage", 1)
            self.cursor.execute(""" SELECT StorageAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(data[0] == 0)  # Set it to One First

            # Repeat For Printer
            self.Database.Assign("Printer", 1)
            self.cursor.execute(""" SELECT PrinterAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(data[0] == 1)
            Success = self.Database.DeAssign("Printer", 1)
            self.cursor.execute(""" SELECT PrinterAccess
                                    FROM employees
                                    Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(data[0] == 0)

            # Repeat for Phone
            self.Database.Assign("Phone", 1)
            self.cursor.execute(""" SELECT PhoneAccess
                                   FROM employees
                                   Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(data[0] == 1)
            Success = self.Database.DeAssign("Phone", 1)
            self.cursor.execute(""" SELECT PhoneAccess
                                   FROM employees
                                   Where id = 1""")
            data = self.cursor.fetchone()
            self.assertTrue(data[0] == 0)

if __name__ == "__main__":
    unittest.main()
