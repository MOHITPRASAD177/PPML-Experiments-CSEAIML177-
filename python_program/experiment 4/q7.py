#fibonacci series upto n terms
n=int(input("Enter number of terms: "))
a,b=0,1
count=0
while(count<n):
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
    