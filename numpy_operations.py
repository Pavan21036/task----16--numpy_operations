
import numpy as np

print("---- 1. Creating Arrays ----")

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3)


print("\n---- 2. Mathematical Operations ----")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


print("\n---- 3. Broadcasting ----")

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([10, 20, 30])

print("Broadcasting Result:\n", x + y)


print("\n---- 4. Statistical Functions ----")

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))


print("\n---- 5. NumPy vs Python List ----")

import time

# Python List
list_data = list(range(1000000))
start = time.time()
list_result = [x * 2 for x in list_data]
print("List Time:", time.time() - start)

# NumPy Array
numpy_data = np.arange(1000000)
start = time.time()
numpy_result = numpy_data * 2
print("NumPy Time:", time.time() - start)


print("\n---- 6. Random Data Generation ----")

random_array = np.random.rand(3, 3)
print("Random 3x3 Array:\n", random_array)


print("\n---- 7. Optimized Calculations ----")

large_array = np.arange(1000000)
print("Optimized Sum:", np.sum(large_array))


print("\n---- 8. Array Structure ----")

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)
