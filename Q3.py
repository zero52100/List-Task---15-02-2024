"""
Q3.3.Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3"""
list=[]
limit = int(input("Enter number of elements to be insert into to list: "))
for i in range(limit):
    list.append((input(f"Enter {(i+1)}th string : ")))
count=0
for i in list:
    if len(i)>2:
        count += 1
if count>0:
    print(f"Total {count}  string are have lenght {limit} or more limit ")
else:
    print(f"All lenght of string in the {list}below 2 ")