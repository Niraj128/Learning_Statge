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
