import sqlite3
class Paginator:
    def __init__(self):
        self.connection =conn = sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.list=[]
        self.Paginate()


    def Paginate(self):
       self.cursor.execute(""" SELECT * FROM employees""")
       inner=[]
       count=0;
       for row in self.cursor:
           count+=1
           inner.append(row)
           if count%10==0:
               self.list.append(inner)
               inner=[]

       if count %10 < 10:
            self.list.append(inner)





    def ListAll(self):
      print("hello")
      list=self.list
      count = 1
      for row in list:
          print("Page number "+str(count))
          count +=1;
          for inner in row:
            print(inner)
          print('\n')

    def ListOne(self , number):
      if(number < len(self.list)):
       innerList =self.list[number]
       count=1
       for row in innerList:
          print(row)
      else:
          print("No Page with this number")
