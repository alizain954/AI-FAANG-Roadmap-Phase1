# conditional if else and elif

num = int(input('Enter the age: '))
if num >= 18:
    print('You are adult')
elif num >= 13:
    print('You are teenager')
else:
    print('You are child')
    
# condition operator
# there are following operator which are used
# > greater
# < less 
# >= greather then equcal too
# <= less then equcal too
# != not equcal too

# there lecture for the loop 

# there are two loop in python for , while 

for i in range(0, 10):
    print(i)
    
# range have 3 paramter range(start, end, stop)
# but at the last this is not include means uper case 10 is not print 

for i in range(11, 21, 2):
    print(i)

# while loop
# Loop runs as long as condition is true

i = 0
while i <= 5:
    print(f'ali zain is here {i}')
    i = i + 1 # here is the increment of the i 
    # we can do the increment like this i+=1 

# there is 3 function are used in loop 
# break, continue, pass
# Break ( it means loop break on that condition means like return)
# continue ( its means loop skip this condition move forward)
# pass ( it do nothing like pass it )
# and(when both are true) , or(when 1 is true),  not

for i in range(5):
    if i == 3:
        break     # exit loop
    print(i)

for i in range(5):
    if i == 2:
        continue  # skip this loop
    print(i)

# Nested Loops 
# when we used the loop inside the loop
for i in range(3):
    for j in range(2):
        print(f"{i} - {j}")
# patten star

for i in range(1, 6):
    print("*" * i)

#Assigment 1 
# Ask user for a number and print whether it's odd or even.

num = int(input("enter number here: "))

if num % 2 == 0:
    print('this Number is Even')
else:
    print('this Number is Odd')
    
# Assigment 2
# Print numbers from 1–50. If divisible by 3, print "Fizz", by 5 print "Buzz", by both print "FizzBuzz".

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Assigment 3
# Mock: if age > 50 and has symptoms => high risk

age = int(input("Enter age: "))
symptoms = input("Do you have symptoms (yes/no): ")

if age > 50 and symptoms.lower() == "yes":
    print("High Risk")
else:
    print("Low Risk")

#Write a function that finds the maximum value in a list without using max() function.

def fun_max(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num

print(fun_max([1, 3, 2, 5, 8, 4, 9, 10, 6]))