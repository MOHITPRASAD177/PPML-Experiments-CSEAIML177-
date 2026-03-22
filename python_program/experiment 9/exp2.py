#program using lambda function
S = lambda n: n*n
print(S(4))

#program using map function
l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)    