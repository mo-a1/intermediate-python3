from functools import partial


def bigger_than(a, b):
    return a > b


bigger_than_10 = partial(bigger_than, 10)

print(bigger_than(10, 5))
print(bigger_than_10(5))
print(bigger_than_10(20))
