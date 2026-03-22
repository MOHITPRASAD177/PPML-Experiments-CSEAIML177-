class Class1:
    def addition(self,num1,num2):
        print("addition",num1+num2)
class Class2:
    def subtraction(self,num1,num2):
        print("subtraction",num1-num2)
class Class3:
    def multiplication(self,num1,num2):
        print("multiplication",num1*num2)
class Class4:
    def division(self,num1,num2):
        if num2!=0:
            print("division",num1/num2)
        else:
            print("division by zero is not allowed")
class Derived(Class1,Class2,Class3,Class4):
    def __init__(self,data1,data2):
        self.num1=data1
        self.num2=data2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))        
obj = Derived(num1,num2)
obj.addition(num1,num2)
obj.subtraction(num1,num2)
obj.multiplication(num1,num2)
obj.division(num1,num2)