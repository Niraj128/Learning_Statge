#Inheritence in python

#Base class aka "Parent class"
class person():
    def __init__(self,name):
        self.name = name

    def displayName(self):
        print(self.name)

#By default we can say particular person is unmemployed
    def isEmployed(self):
        print(self.name, "is un-Employed !!")

#Derived class aks "Child class"

class Employee(person):
    def isEmployed(self):
        print(self.name, "is Employed !!")


emp = person('Niraj')
emp.displayName()
emp.isEmployed()

emp1 = Employee('Niraj')
emp1.displayName()
emp1.isEmployed()


#Inheritence in python

#How to initialise constructor of base class? 

#Base class aka "Parent class"
class person():
    def __init__(self,name):
        self.name = name

    def displayName(self):
        print(self.name)

#By default we can say particular person is unmemployed
    def isEmployed(self):
        print(self.name, "is un-Employed !!")

#Derived class aks "Child class"

class Employee(person):

    def __init__(self, emp_name,id_num,salary,designation):
        self.idnumber = id_num
        self.emp_salary = salary
        self.emp_designation = designation
        
        #Calling constructor of base class
        #person.__init__(self, emp_name)
        super,__init__(emp_name)

    def isEmployed(self):
        print(self.name, "is Employed !!")

