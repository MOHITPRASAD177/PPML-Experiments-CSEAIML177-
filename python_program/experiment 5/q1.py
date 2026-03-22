#generate fibonacci series between 0 to 1000 then find sum of even valued terms
a,b=0,1
sum_even=0
print("Fibonacci series up to 1000 is:")
while a<=1000:
    print(a,end=' ')
    if a%2==0:
        sum_even+=a
    a,b=b,a+b
print("Sum of even valued terms in Fibonacci series up to 1000 is:",sum_even)
