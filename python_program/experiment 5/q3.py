#find the fahrenheit for a given celsius from the list
celsius_list=[0,10,20,30,40,50,60,70,80,90,100]
print("Celsius to Fahrenheit conversion:")
for celsius in celsius_list:
    fahrenheit=(celsius*9/5)+32
    print(f"{celsius}°C = {fahrenheit}°F")
    