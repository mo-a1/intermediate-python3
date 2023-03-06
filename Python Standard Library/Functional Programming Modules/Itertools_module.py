import itertools

# Itertools module
#   - .count() -> start, step
#   - .zip_longest()
#   - .cycle(iterable)
#   - .repeat() --> rare use
#   - .starmap() --> rare use
#   - .combinations()
#   - .permutations()
#   - .product()
#   - .islice() -> used to get a slice from an iterator or iterable
#                           ->> very useful method specially when work with large files
#   - .compress()
#   - .groupby()
#   - .tee() -> make a copy or more of the original iterator but after that we must use the copies not the original one.

days = [55, 56, 57, 58, 59, 60, 61, 62]
a = zip(itertools.count(), days)

print(list(next(a) for i in range(2)))

for i in a:
    print(i)

print('*1' * 30)

print(list(itertools.zip_longest(range(10), days)))

print('*2' * 30)

cycle = itertools.cycle([1, 2, 3])
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

print('*2.5' * 30)

cycle_2 = itertools.cycle(('on', 'off'))
print(next(cycle_2))
print(next(cycle_2))
print(next(cycle_2))
print(next(cycle_2))
print(next(cycle_2))
print(next(cycle_2))

print('*3' * 30)

list_1 = ['a', 'b', 'c', 'd']
result_1 = itertools.combinations(list_1, 2)
n = 1
for i in result_1:
    print(i, n)
    n += 1

print('*4' * 30)

result_2 = itertools.permutations(list_1, 2)
n = 1
for i in result_2:
    print(i, n)
    n += 1

print('*5' * 30)

list_2 = [1, 2, 3, 4]
result_3 = itertools.product(list_2, repeat=4)
n = 1
for i in result_3:
    print(i, n)
    n += 1

print('*6 ' * 30)

result_4 = itertools.product(list_1, list_2)
n = 1
for i in result_4:
    print(i, n)
    n += 1

print('*7 ' * 30)

with open(r'testing_files/large.txt', 'r') as file:
    for line in itertools.islice(file, 100, 105):
        print(line, end='')

print('*8 ' * 30)

selectors = [True, False, True, True]

result_5 = itertools.compress(list_1, selectors=selectors)
n = 1
for i in result_5:
    print(i, n)
    n += 1

print('*9 ' * 30)

copy_1, copy_2 = itertools.tee(result_5)
print(copy_1)
print(copy_2)
for i in copy_1:
    print(i)
print('it will not print any thing because the original iterator is exhausted')
