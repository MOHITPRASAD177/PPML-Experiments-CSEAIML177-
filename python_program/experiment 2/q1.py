principle= int(input("Enter the principal amount: "))
rate= float(input("Enter the rate of interest: "))
time= int(input("Enter the time in years: "))
simple_interest = (principle * rate * time) / 100
amount = principle * ((1+rate/100)**time)
compund_interest= amount - principle
print("Simple Interest is:", simple_interest)
print("Compound Interest is:", compund_interest)