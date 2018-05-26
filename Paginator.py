import sqlite3
class Paginator:
    #Initialize Object
    def __init__(self):
        self.connection =conn = sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.list=[]
        self.Paginate()

    # Make a list of Lists of tuples with 10 as the size of each inner List
    def Paginate(self):
       self.cursor.execute(""" SELECT * FROM employees""")
       innerRow=[]
       count=0;
       for row in self.cursor:
           count+=1
           innerRow.append(row)
           if count%10==0:
               self.list.append(innerRow)
               innerRow=[]

       if count %10 < 10:
            self.list.append(innerRow)




    #List all elements inside the Paginator
    def ListAll(self):
      print("hello")
      list=self.list
      count = 1
      phoneAccess="None"  #Make Bits into String
      StorageAccess="None"
      PrinterAccess="None"
      for row in list:
          print("Page number "+str(count))
          count +=1;
          for innerRow in row:
            if innerRow[4] == 1:
                phoneAccess="Yes"
            if innerRow[5] == 1:
                PrinterAccess="Yes"
            if innerRow[6] == 1:
                StorageAccess="Yes"
            print(" ID "+str(innerRow[0])+" Name "+innerRow[1]
               +" Email "+innerRow[3]+" Phone Access "+phoneAccess+
               " Printer Access "+PrinterAccess
               +" Storage Access "+StorageAccess)
            phoneAccess="None"
            StorageAccess="None"
            PrinterAccess="None"
          print('\n')
    #Given a Page number .. List elements in it
    def ListOne(self , number):
      if(number < len(self.list)):
        innerList =self.list[number]
        count=1
        phoneAccess="None"
        StorageAccess="None"
        PrinterAccess="None"
        for innerRow in innerList:
            if innerRow[4] == 1:
                phoneAccess="Yes"
            if innerRow[5] == 1:
                PrinterAccess="Yes"
            if innerRow[6] == 1:
                StorageAccess="Yes"
            print(" ID "+str(innerRow[0])+" Name "+innerRow[1]
               +" Email "+innerRow[3]+" Phone Access "+phoneAccess+
               " Printer Access "+PrinterAccess
               +" Storage Access "+StorageAccess)
            phoneAccess="None"
            StorageAccess="None"
            PrinterAccess="None"

      else:
          print("No Page with this number")
