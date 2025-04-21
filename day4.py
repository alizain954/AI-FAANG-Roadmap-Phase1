# today we see the data structure of python
# list, tuple, set, dict

# List(ordered, mutable, duplicated allow, )

my_list = [10, 20, 30]
print(my_list[0])       # 10

my_list.append(40)      # [10, 20, 30, 40]
my_list.remove(20)      # [10, 30, 40]
my_list[1] = 99         # [10, 99, 40]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


# Useful List Methods:
# append(), extend(), insert()
# pop(), remove(), clear()
# sort(), reverse()
# index(), count()

# Tuples (Ordered, Immutable)

my_tuple = (1, 2, 3)
print(my_tuple[0])       # 1

# Faster than lists
# Used for fixed data, like (latitude, longitude)

