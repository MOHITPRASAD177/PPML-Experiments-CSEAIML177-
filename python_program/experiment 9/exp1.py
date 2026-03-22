#positional arguments
def add(a,b):
    return a+b
print(add(5,10))

#program using positional arguments
def product(a,b):
    print("Product=",a*b)
product(4,6)

#keyword arguments
def display(name,age):
    print(name,age)
display(age=20,name="Ravi")

#program using keyword arguments
def student(name,course):
    print("Name:",name)
    print("Course:",course)
student(course="Python",name="Anu")

#default arguments
def greet(name="Student"):
    print("Hello",name)
greet()

#program using default arguments
def bill(amount=100):
    print("Bill amount:",amount)
bill(500)
bill()

#arbitrary arguments, program using *args
def total(*nums):
    print("Sum=",sum(nums))
total(10,20,30)

#program using **kwargs
def employee(**details):
    for k,v in details.items():
        print(k,":",v)
employee(name="Mohit",id=101,dept="IT")                    