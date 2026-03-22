def check_prime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:  cnt = cnt+1
    if cnt>2 : print("not prime")
    else : print("prime")
num = int(input("Enter a number: "))
check_prime(num)