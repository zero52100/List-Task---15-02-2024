"""
Q7.Write a Python program to find the repeated items of atuple."""
list=[]

limit = int(input("Enter number of elements to be insert into to tuple: "))
for i in range(limit):
    list.append(int(input(f"Enter {(i+1)}th elements : ")))
tuple1 = tuple(list)
repeated = []
for item in tuple1:
    if tuple1.count(item) > 1 and item not in repeated:
        repeated.append(item)

if len(repeated)==0:
    print("No repeated items in the tuple. ")
else:
    print(repeated)
