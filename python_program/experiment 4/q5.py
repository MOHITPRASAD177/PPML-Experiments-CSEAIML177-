#test a number is palindrome or not
num=int(input("Enter a number: "))
rev=0
temp=num
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if(rev==num):
    print("Palindrome")
else:
    print("Not Palindrome")
    