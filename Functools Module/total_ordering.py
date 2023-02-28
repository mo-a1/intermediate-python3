import functools
from functools import total_ordering

# https://www.youtube.com/watch?v=Jztj_yuFTlk&ab_channel=IndianPythonista
"""
Note: While this decorator makes it easy to create well behaved totally ordered types, it does come at the cost of
    slower execution and more complex stack traces for the derived comparison methods. If performance benchmarking
    indicates this is a bottleneck for a given application, implementing all six rich comparison methods instead is
    likely to provide an easy speed boost.
    
Note: This decorator makes no attempt to override methods that have been declared in the class or its superclasses.
    Meaning that if a superclass defines a comparison operator, total_ordering will not implement it again,
    even if the original method is abstract.
"""

print("------------------------- @total_ordering ----------------------")


@total_ordering
class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data


a = Node(10)
b = Node(20)

print(b > a, " = ", b.__gt__(a), " despite of we did not define the __gt__ method")

