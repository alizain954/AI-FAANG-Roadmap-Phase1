
from functools import reduce

# Lambda Fucntion

# Find the square

x = lambda y : y**2
print(x(5))

# Add two number 

y = lambda a, b : a + b
print(y(7, 8))

# check the even

z = lambda x: x % 2 == 0

print(z(12))

# Filter.....

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x%2==0, nums))
print(even)


words = ['ali', '', 'zain', 'google', '']

empty_str = list(filter(lambda x: x!= '', words))
print(empty_str)

ages = [12, 45, 26, 14 , 78, 11, 87, 4]

age_checks = list(filter(lambda x: x >= 18, ages))
print(age_checks)


# Map ..................

square = [1, 2, 3, 4]

sqr = list(map(lambda x:x**2, square))
print(sqr)

names = ['Bilal', 'Ali', 'Zain', 'paksiatn']

name_upper = list(map(lambda x: x.upper(), names))
print(name_upper)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_mul = list(map(lambda x: x*2, num))
print(num_mul)


# reduce

add = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

add_list = reduce(lambda x, y: x + y, add)
print(add_list)

nums = [2, 3, 4]

num_mul = reduce(lambda x, y:x*y, nums)
print(num_mul)

words = ['Ali', 'Zain', 'is', 'good', 'boy']

senstence = reduce(lambda x, y: x + ' ' + y, words)
print(senstence)


# Zip............

names = ["Ali", "Zain", "Ahmed"]
scores = [90, 85, 88]

pair = list(zip(names, scores))
print(pair)


a = [1, 2, 3]
b = [4, 5, 6]
sums = [x + y for x, y in zip(a, b)]
print(sums)


letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter, number in zip(letters, numbers):
    print(letter, number)


# enumerate ...........

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


colors = ["red", "blue", "green"]
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")


languages = ["Python", "Java", "C++"]
indexed = list(enumerate(languages))
print(indexed)


# lambda	    Naam ke bina chhota function	             Anonymous function for short operations
# map()	        Har item par function apply karta hai	     Applies function to each element in iterable
# filter()	    Sirf True wale items ko return karta hai	 Filters items based on a condition
# reduce()	    Sab items ko combine karta hai	             Reduces sequence to single value
# zip()	        Lists ko pair bana kar combine karta hai	 Combines iterables element-wise into tuples
# enumerate()	List ke item ke sath index bhi deta hai	     Adds index during iteration
