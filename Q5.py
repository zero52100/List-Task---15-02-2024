"""
Q5.5.Use list comprehension to contruct a new list but add 6 to each item.
	list = [24,34,54,45]"""

list=[]
limit = int(input("Enter number of elements to be insert into to list: "))
for i in range(limit):
    list.append(int(input(f"Enter {(i+1)}th elements : ")))
new_list=[]


for i in list:
    new_list.append(i+6)

print(f"The list after adding 6 : {new_list}")