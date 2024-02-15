"""
Q4.4.Write a Python program to print the numbers of a specified listafter removing even numbers from it
	list = [24,34,53,65,78,93,23,42]"""


list1=[]
limit = int(input("Enter number of elements to be insert into to list: "))
for i in range(limit):
    list1.append(int(input(f"Enter {(i+1)}th elements : ")))
list_odd=[]
for i in list1:
    if(i%2!=0):
        list_odd.append(i)
if len(list1)==len(list_odd):
    print("THere no even number in the limit user entered")
else:
    print(f"The list after removing even number {list_odd}")

