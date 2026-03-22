def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
print("Simple Interest is:", simple_interest(principal, rate, time))