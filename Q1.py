"""
Q1.1.Write a Python program to multiples all the items in a list."""

list1=[1,2,4,5,6]
range=int(input("enter the number to multiples all the items in a list :"))
result=[]
for i in list1:
    result.append(i*range)

print(result)