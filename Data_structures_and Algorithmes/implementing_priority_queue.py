# Priority queue ===== صف مرتب بالأولوية
import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, priority: int, item):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        priority, *ign = heapq.heappop(self._queue)
        priority *= -1
        return priority, ign[0], ign[1]


pq = PriorityQueue()
pq.push(priority=1, item=['ali', 95])
pq.push(priority=3, item=['morad', 78])
pq.push(priority=3, item=['sayed', 90])
pq.push(priority=1, item=['mona', 98])

print(pq.pop())
print(pq._queue)