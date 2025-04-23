# File Handle 

name = input('Enter Your name: ')
age = int(input('Enter your age: '))

f = open('data.txt', 'a') 
f.write(name + ' ' + str(age) + '\n')
f.close()

# Now read the file and print content
fa = open('data.txt', 'r')
content = fa.read()
print("\nCurrent File Content:\n")
print(content)
fa.close()


# Modules

from modules import add, sub, sub1, mul

add(12, 13)
sub(32, 12)
mul(23, 2)
sub1(16, 2)

# Generator

def gen_sub():
    yield range(0, 6)  # Ye ek hi dafa pura range object dega

call_gen = gen_sub()

for i in call_gen:
    for num in i:  # Range ke andr values iterate karo
        print(num)
        
        
def even_generator():
    for num in range(0, 21):  # 0 to 20 tak loop
        if num % 2 == 0:
            yield num  # Agar even ho to return karo

# Generator ko call karo
even_nums = even_generator()

# Loop se values print karo
for i in even_nums:
    print(i)


def letter_generator(text):
    for char in text:
        yield char  # har dafa ek letter return karega

# Generator ko call karo
gen = letter_generator("Malik Zain")

# For loop se print karo
for letter in gen:
    print(letter)
    
    

#Decorators

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hi():
    print("Hi")

say_hi()


def greet_decorator(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
        print("Goodbye!")
    return wrapper

@greet_decorator
def say_hello(name):
    print(f"Hello {name}")

say_hello("Malik")


