import copy

"""
The difference between shallow and deep copying is only relevant for compound objects
 (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the
 objects found in the original.

A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the
 original.
"""
print("----------------- shallow copy -------------------")

a = [1, 2, 3, 4, 5, 6]
copy_a = a[:]
print(copy_a)

b = [[2, 4], [6, 8]]
copy_b = b[:]
copy_b[0][0] = 999
print("b 'the original one' => ", b)
# Note that in shallow copy only the main object is copied
# and its nested objects only assigned to the original ones values

dct = {}
copy_dct = dct.copy()  # shallow copy

print("----------------- deep copy -------------------")

lis = [1, [2, 3], [4, 5]]
copy_lis = copy.deepcopy(lis)
print(copy_lis)
lis[0] = 99
lis[1][0] = 5578
print("lis = ", lis)
print("copy_lis = ", copy_lis)

print("----------------- not copy -------------------")

# NOTE: this is not copy it is just assign a reference of list x to variable z,
# so using '=' operator doesn't make copies

x = [1, 2, 3, 4, 5]
z = x
z[0] = 99
print(x)  # [99, 2, 3, 4, 5]
