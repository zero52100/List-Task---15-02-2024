"""
Q7.Write a Python program to find the repeated items of atuple."""

tuple = (1, 2, 3, 2, 4, 5, 6, 4, 7, 8,9,10,9,12,11,12)
repeated = []
for item in tuple:
    if tuple.count(item) > 1 and item not in repeated:
        repeated.append(item)
print(repeated)
