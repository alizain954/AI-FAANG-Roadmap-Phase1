# function
def greet(name):
    return f"Hello, {name}!"

print(greet("Malik"))

# Defien parameter default and keyword
def fun_defult(name='Ali Zain'):
    return f'hello {name}'

show = fun_defult()
print(show) 
show1 = fun_defult(name='FAANG')
print(show1)

# Positional vs Keyword Arguments

def full_name(first, last):
    print(f"{first} {last}")

full_name("Ali", "Zain")               # Positional
full_name(last="Zain", first="Ali")    # Keyword

# *args: Accepts multiple positional arguments
def add(*nums):
    return sum(nums)

print(add(2, 3))           # 5
print(add(1, 2, 3, 4))     # 10

# **kwargs: Accepts key=value pairs
def profile(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

profile(name="Ali", age=26)

# Lambda
square = lambda x: x**2
print(square(4))  # Output: 16

add = lambda a, b: a + b
print(add(3, 5))  # Output: 8

# Function Nesting & Returning Functions
def outer():
    def inner():
        print('inner function')
    inner()

outer()

def multiplier(x):
    return lambda y: x * y

double = multiplier(2)
print(double(5))  # Output: 10

#Find the Factorial of a Number using Recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))