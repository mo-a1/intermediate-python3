from collections import ChainMap

a = {
    "blue": 2,
    "red": 3
}

b = {
    "yellow": 1,
    "green": 4
}

c = ChainMap(a, b)
print(c)
print(c["green"])

for i, j in c.items():
    print(i, j)

print(c.new_child({"black": 0}))
print(c.maps)
print(c)

print(c.popitem())
c[3] = 5
