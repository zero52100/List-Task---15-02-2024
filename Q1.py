"""
Q1.1.Write a Python program to multiples all the items in a list."""

list1=[]
limit = int(input("Enter number of elements to be insert into to list: "))
for i in range(limit):
    list1.append(int(input(f"Enter {(i+1)}th elements : ")))
range=int(input("enter the number to multiples all the items in a list :"))
result=[]
for i in list1:
    result.append(i*range)
print(f"List before mutlipy the list  :{list1}")
print(f"List after multipying with {limit } : {result}")