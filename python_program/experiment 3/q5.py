total=0
for i in range (1,6):
    m=int(input("enter the marks"))
    total+=m
    per=(total/250)*100
if per>=90:
        print("garde O")
elif per>=80:
            print("grade E")
elif per>=70:
                print("grade A")
else:
                    print("grade B")