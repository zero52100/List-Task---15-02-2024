"""
Q6..Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]"""

list1=[]
limit = int(input("Enter number of elements to be insert into to list: "))
for i in range(limit):
    list1.append(int(input(f"Enter {(i+1)}th elements : ")))
sqr_list=[]
sqr=0

for i in list1:
   
    sqr=(i*i)
    if sqr>50:
        sqr_list.append(sqr)
if len(sqr_list)==0:
    print("Square of all the number in the list is below 50")
else:
    print(sqr_list)