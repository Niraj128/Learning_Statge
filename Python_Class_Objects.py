# How to create a class in python???

# Class of employees in an organisation

class Employee:
    #Constructor of a class
    # It is mainly used for assignment of instance variables
    def __init__(self, name, salary):
        #instance attributes
        self.name = name
        self.emp_sal = salary

    #Method of a class
    def displayEmployeeInfo(self):
        print("Employee Name : ",self.name,"Employee Salary : ",self.emp_sal)

emp1 = Employee('Niraj', 25000)
emp2 = Employee('Preeti', 3000)
emp3 = Employee('Duggu', 100)

emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()
emp3.displayEmployeeInfo()
