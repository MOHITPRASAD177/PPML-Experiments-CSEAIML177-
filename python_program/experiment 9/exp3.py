#program using filter function
ages=[5,12,17,18,24,32]
def myfunc(x):
    if x<18: return False
    else: return True
adults=filter(myfunc,ages)
for x in adults:
    print(x)
    
    

# wap using reduced function
from functools import reduce
words = ["hello"," ","world","!"]
sentence = reduce(lambda x,y: x+y,words)
print("concatenated string:",sentence)    