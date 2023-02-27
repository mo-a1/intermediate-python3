from functools import reduce, singledispatch, wraps

# https://www.youtube.com/watch?v=Jztj_yuFTlk&ab_channel=IndianPythonista

print("------------------------- .reduce() ----------------------")

# reduce(function, iterable, initializer=None)
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 1*2   *3  *4

print("------------------------- @singledispatch ----------------------")


@singledispatch
def add_one(item):
    print("unsupported type")
    return item


@add_one.register(list)
def _(item):
    return item + [1]


@add_one.register(set)
def _(item):
    return item.union({1})


@add_one.register(str)
def _(item):
    return item + str(1)


print(add_one([2, 5, 6, 8]))
print(add_one({10, 2, 5, 300, 6, 8}))
print(add_one("lkl"))
print(add_one(1))

