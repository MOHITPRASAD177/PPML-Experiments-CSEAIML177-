def gcd (x,y,z):
    hcf=1
    for i in range(1,min(x,y,z)+1):
        if(x%i==0 and y%i==0 and z%i==0):
            hcf=i
    return hcf
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
print("GCD of three numbers is: ",gcd(num1,num2,num3))
