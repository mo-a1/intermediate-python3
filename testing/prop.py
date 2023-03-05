from weakref import ref, getweakrefcount, getweakrefs
import fractions


class Node:
    def __init__(self, data):
        self.data = data


a = Node(10)
b = a
aa = ref(a)
# a = None
# print(b.data)
print(aa)
print(getweakrefcount(a))
