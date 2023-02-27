from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENS WOOD', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

rows.sort(key=itemgetter('date'))
# print(rows)

print([i for i in groupby(rows, key=itemgetter('date'))])

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for row in items:
        print('\t', row)

l = [1,2,'l',3]

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ints = list(filter(is_int, l))
print(ints)
