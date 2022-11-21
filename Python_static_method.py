#What is static method in python?

class car:

    def __init__(self, name, color):
        self.car_name = name
        self.color = color

    def displayCarDetails(self):
        print("Car name is : ", self.car_name,"Color of car is : ",self.color)

    @staticmethod
    def welcomeMessage():
        print("Nice Car !!!!!")

car1 = car('Xuv700', 'Red')

car1.displayCarDetails()
car1.welcomeMessage()

# 2nd class example (Satic employee of an organisation)

class Employee:
    
    @staticmethod
    def isEmployeeOf():
        print("I am an employee of Pinelabs!!")

Employee.isEmployeeOf()


