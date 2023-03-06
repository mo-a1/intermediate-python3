import heapq

nums = [5, 16, 2, 3, 17, 65, 6, 12, 5, 3, 62, 698, 5156, 2, 14, 25, 8]
heapq.heapify(nums)

print(heapq.nlargest(4, nums))
print(heapq.nsmallest(4, nums))

data = [
    {'name': 'ali', 'age': 17},
    {'name': 'salma', 'age': 27},
    {'name': 'hoda', 'age': 19},
    {'name': 'sayed', 'age': 35},
    {'name': 'kareem', 'age': 41},
]

oldest_people = heapq.nlargest(2, data, key=lambda a: a['age'])  
print(oldest_people)

youngest_pople = heapq.nsmallest(2, data, lambda a: a['age'])
print(youngest_pople)

name_sort = heapq.nsmallest(2, data, key=lambda a: a['name'])
print(name_sort)
