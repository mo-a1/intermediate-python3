from collections import deque

# NOTE: the behavior of all methods to work on the right side, to work on the left side we use: popleft,
#  appendleft, extendleft, etc..

d = deque([1], maxlen=8)
d.appendleft(0)
d.appendleft(-1)
print(d)
d.appendleft(-2)
print(d)
print(d.maxlen)

print("\n", "1 == " * 20, "\n")

d.rotate(1)   # rotate right (move all element 1 step to right)
print(d)
d.rotate(-1)   # rotate left (move all element 1 step to left)
print(d)

d.insert(1, 10)
print(d)

print("\n", "2 == " * 20, "\n")

a = d.copy()
print(a)
d.clear()
print(d)

print("\n", "3 == " * 20, "\n")

print(a.count(1))

a.reverse()    # reverse in place (modify the original one)
print(a)
