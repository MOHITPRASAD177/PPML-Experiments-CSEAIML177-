num=int(input("Enter a number: "))
cnt=0
i=1
while(i<=num):
    if(num%i==0):
        cnt=cnt+1
    i=i+1
if(cnt>2):
    print("not Prime")
else:
    print("Prime")