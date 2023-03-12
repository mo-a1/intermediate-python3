import heapq

a = [18, 15, 2, 4, 6, 8, 10, 12, 14]
heapq.heapify(a)
print(a, type(a))   # [2, 4, 8, 12, 6, 18, 10, 15, 14] <class 'list'>

print(heapq.heappushpop(a, 0))  # push then return the smallest item
print(heapq.heapreplace(a, 10))

print(heapq.nlargest(2, a))
print(heapq.nsmallest(3, a))
print(a)
