"""
Q5.5.Use list comprehension to contruct a new list but add 6 to each item.
	list = [24,34,54,45]"""

list = [24,34,54,45]
new_list=[]

for i in list:
    new_list.append(i+6)

print(new_list)