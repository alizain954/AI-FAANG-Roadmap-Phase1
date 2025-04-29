# Numpy

# pip3 install numpy
import numpy as np

my_list = [1, 2, 3, 4]

my_array = np.array(my_list)
print(my_array)
print(type(my_array))

print(my_array.shape)   # Shape: (4,) => 1D array, 4 elements
print(my_array.dtype)   # Data type: int32 ya int64
print(my_array.ndim)    # Number of dimensions: 1

zeros = np.zeros((2, 3))
print(zeros)


ones = np.ones((3, 2))
print(ones)

range_array = np.arange(0, 10, 2)
print(range_array)

lin_array = np.linspace(0, 1, 5)
print(lin_array)


import time

# List Operation
my_list = list(range(1000000))
start = time.time()
my_list = [x + 5 for x in my_list]
print("List Time:", time.time() - start)

# NumPy Operation
my_array = np.arange(1000000)
start = time.time()
my_array = my_array + 5
print("NumPy Array Time:", time.time() - start)
