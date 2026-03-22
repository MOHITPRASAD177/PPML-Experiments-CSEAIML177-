# q4.py - Sum of digits of a positive number
num = int(input("Enter a positive number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("Sum of digits is:", sum_of_digits)