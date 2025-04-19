# we start with variable:
#variable  we store the value or we give name to the value 
# in the left-side variable and right-side the value
#for example:
a = 10

#here a is the varibale name and 10 is the value 
# there is following rules of Naming the variable
# not start with number or special character e.g: 1a, *b, something like this
# varible are the case sensitive like there is a and A is the different
# we can start with _ underscore like , _myName, 
# in varibale name there is no space or character except the underscore like it is wrong, my-Name it is wrong 

print(a) 

#we can write the varible in one like or given value 
#Many Values to Multiple Variables in One Line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Apple"
print(x)
print(y)
print(z)

# Unpack a Collection
fruit = ["Orange", "Banana", "Cherry"]
x, y, z = fruit
print(x)
print(y)
print(z)

# Global varibale and local varibale we see in function lecture


#### String #####

a = "Hello"
print(a)

# the value wrriten in single or duble qutation is know as the string in this character are save 

#string are working like the arrays which index start from 0 and we can access it form index number 
print(a[0]) # here the only world H is print 

#length of string
print(len(a)) # len is the build in function which gives us the length of the string

# check the worl is it in string or not

txt = "The best things in life are free!"
print('free' in txt) # it give us the booleand value True of False
print('Ali' not in txt) # also give True


#Python - Slicing Strings
# slicing mean specific range of index see in the string
b = 'Hello world!'
print(len(b))
print(b[2:]) # start from 2 index and print end of string
print(b[:4]) # start from 0 index and print the 4 index
print(b[3:7]) #statr from 3 and end on 7 but 7 is not print means print before 7 on 6 index
print(b[-5:-2]) #negative indexing statr from the right to left it not start from 0 it start -1

# Number Float and complex in python and also see the boolean datatype

num = 123
num_f = 12.3
num_b = True
num_c = 2+3j

print(num)
print(num_f)
print(num_b)
print(num_c)

# now check the type of the these datatype

print(type(num))
print(type(num_f))
print(type(num_b))
print(type(num_c))

# Now we are using the I/O and Output 

input_num = input('enter the name')
print(input_num)

#By default, input is taken as a string, convert if needed

input_int = int(input('Enter the Number: '))
print(input_int)

# script for bmi calculate

name = input('Enter your name: ')
age = int(input("enter the age: "))
weight = float(input('Enter your weight: '))
height = 1.80

bmi = weight /  height ** 2
print(f"Hello {name}, you are {age} years old. Your BMI is {round(bmi, 2)}.")


# if else condition

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
    
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{age} is churil")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# Loop ( For While, Break, Continues)

a = range(0, 21)
for i in a:
    print(i)

    
# while loop

i = 0

while i <= 10:
    print(f'ali is here, {i}')
    i += 1

# Continue, Break
for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break     # stop at 7
    print(i)

# problem of DSA

name = input('enter the name')
b = ''
for i in name:
    b = i + b

print(b)

    