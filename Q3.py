"""
Q3.3.Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3"""

List= ['abc', 'xyz', 'abc', '1']
count=0
for i in List:
    if len(i)>2:
        count += 1

print(count)