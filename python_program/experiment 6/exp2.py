n=int(input("enter number of element"))
dict1={}
for i in range (n):
         key=input("enter key")
         value=input("enter value")
         dict1[key]=value
dict2={}
for key,value in dict1.items():
    dict2[value]=key
print("first dictionary")
print(dict1) 
print("secondary dictionary")
print(dict2)