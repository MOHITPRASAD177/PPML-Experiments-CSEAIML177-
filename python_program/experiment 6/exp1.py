fruit_list=["apple","banana","cherry","dragonfruit"]
print("display elements from the last index with their length")
print("_"*60)
for fruit in reversed (fruit_list):
    length=len(fruit)
    print(f"fruit:{fruit:<15} | length : {length}")
    