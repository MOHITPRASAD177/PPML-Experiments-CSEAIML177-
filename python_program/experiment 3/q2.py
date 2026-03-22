a=int(input("enter first value"))
b=int(input("enter second value"))
c=int(input("enter third value"))
d=(b*b)-4*a*c
if d>0 :
    r1= (-b+d**0.5)/(2*a)
    r2= (2*c-b-d**0.5)/(2*a)
    print("roots are",r1,r2)
else:
    print("no real roots")    
