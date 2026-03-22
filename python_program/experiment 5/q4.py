#create an empty list and input a group of numbers ,remove the duplicates, sort in ascending order and display the result
numbers=[]
n=int(input("Enter the number of elements you want to add: "))
for i in range(n):
    num=int(input("Enter number: "))
    numbers.append(num)
unique_numbers=list(set(numbers))
unique_numbers.sort()
print("Sorted list after removing duplicates:",unique_numbers)
   