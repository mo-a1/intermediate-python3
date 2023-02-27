from collections.abc import Iterable

# stop when the lambda returns 2

lis = [1, 2, 3, 4, 5]
a = iter(lambda: lis.pop(), 2)

for i in a:
    print(i)

# flatting nested sequence

n_l = [1, [2, [3, 4], 5, 6], 7]


def flatted(items, ign_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ign_types):
            yield from flatted(x)
        else:
            yield x


print([i for i in flatted(n_l)])

