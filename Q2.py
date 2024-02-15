"""
Q2.Write a Python program to remove duplicates from a list,"""

"""
2.Write a Python program to remove duplicates from a list,"""

list1=[1,2,4,5,5,6]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)