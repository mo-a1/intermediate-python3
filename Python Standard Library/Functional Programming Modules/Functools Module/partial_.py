from functools import partial


def smaller_than(a, b):
    return a > b


smaller_than_10 = partial(smaller_than, 10)

print(smaller_than(10, 5))
print(smaller_than_10(5))
print(smaller_than_10(20))
