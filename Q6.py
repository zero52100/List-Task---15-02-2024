"""
Q6..Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]"""

lst1=[2, 4, 6, 8, 10, 12, 14]
sqr_list=[]
sqr=0

for i in lst1:
   
    sqr=(i*i)
    if sqr>50:
        sqr_list.append(sqr)

print(sqr_list)