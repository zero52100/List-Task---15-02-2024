"""
Q4.4.Write a Python program to print the numbers of a specified listafter removing even numbers from it
	list = [24,34,53,65,78,93,23,42]"""

list = [24,34,53,65,78,93,23,42]
list_odd=[]

for i in list:
    if(i%2!=0):
        list_odd.append(i)

print(list_odd)

