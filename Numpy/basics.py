import numpy as np

my_array = np.array([[1, 2], [3, 4]])

print(my_array)
print(my_array[1])
print(my_array[1][0])
print(my_array[1, 0])

print('*1 ' * 20)
_array_1 = np.array([[1, 2]], ndmin=3)
print(_array_1)

# num of diminutions
print(my_array.ndim, 'diminutions')
print(_array_1.ndim, 'diminutions')

print('# Slicing ' * 5)
# Slicing

_array_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
_array_3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])

print(_array_2.ndim, 'diminutions')
print(_array_2[2, 2:])
print(_array_2[2:4, 0:2])

print(_array_3.ndim, 'diminutions')
print(_array_3[1, 0, 0:2])

