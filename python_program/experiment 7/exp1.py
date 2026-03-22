m = int(input("Enter the starting number: "))
n = int(input("Enter the ending number: "))
num_list = []
for i in range(m, n + 1):
    num_list.append(i)
print("List of numbers:", num_list)
total = sum(num_list)
average = total / len(num_list)
largest = max(num_list)
smallest = min(num_list)
print("Sum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
new_list = []
for num in num_list:
    if num % 3 != 0:
        new_list.append(num)
print("List excluding numbers divisible by 3:", new_list)