#program that loops over a sequence of elements of a list,tuple,dictionary and set
list=[1,2,3,4,5]
tuple=(6,7,8,9,10)
dictionary={'a':11,'b':12,'c':13}
set={14,15,16,17,18}
print("list:")
for item in list:
    print(item,end=' ')
print("\ntuple:")
for item in tuple:
    print(item,end=' ')
print("\ndictionary:")
for key,value in dictionary.items():
    print(f"{key}: {value}")
print("set:")
for item in set:
    print(item,end=' ')