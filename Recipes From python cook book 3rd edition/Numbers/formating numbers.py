x = 1234.56789

f_number = format(x, '0.2f')
print(f_number)

print('*' * 30)

f_number = format(x, '>10.2f')
print(f_number)

print('*' * 30)

f_number = format(x, '<10.1f')
print(f_number, '____')

print('*' * 30)

f_number = format(x, '^10.2f')
print(f_number, '____')

print('*' * 30)

f_number = format(x, ',')
print(f_number)

print('*' * 30)

f_number = format(x, ',')
print(f_number)

print('*' * 30)

print(x.__format__('0.1f'))

print('%0.2f' % x)

