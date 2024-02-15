"""
Q2.Write a Python program to remove duplicates from a list,"""

"""
2.Write a Python program to remove duplicates from a list,"""

list1=[]
limit = int(input("Enter number of elements to be insert into to list: "))
for i in range(limit):
    list1.append(int(input(f"Enter {(i+1)}th elements : ")))
list2=[]

for i in list1:
        if i not in list2:
            list2.append(i)

 

if len(list1)==len(list2):
    print("There no duplicate element in the list ")
else:
        print(f"List after removing duplicate element {list2}")