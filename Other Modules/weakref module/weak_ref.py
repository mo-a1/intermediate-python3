import weakref
from sys import getrefcount

# the benefit of it that if the main object deleted all the variables assigned to its reference will be assigned to None
# (if the original reference collected [garbage collected] then it will be garbage from all memory locations)

# https://docs.python.org/3/library/weakref.html#
# https://www.youtube.com/watch?v=GGKerIMqHCk&ab_channel=anthonywritescode


class SomeClass:
    def __init__(self, num):
        self.num = num

    def __del__(self):
        del self.num


a = SomeClass(1)
print("a = ", a)
b = weakref.ref(a)  # <weakref at 0x000001CD24F6A2A0; to 'SomeClass' at 0x000001CD24B7EC50>
# b = a
print("call b ===> ", b)
print("count references to object 'a' = ", getrefcount(a))
print("*" * 50)

a = "some another value"
print("a = ", a)
print("call b ===> ", b)    # <weakref at 0x000001CD24F6A2A0; dead>
print("count references to object 'a' = ", getrefcount(a))
