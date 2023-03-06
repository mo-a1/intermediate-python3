import queue


# The module implements three types of queue, which differ only in the order in which the entries are retrieved.

# 1- FIFO queue, the first tasks added are the first retrieved.
# 2- LIFO queue, the most recently added entry is the first retrieved (operating like a stack).
# 3- Priority queue, the entries are kept sorted (using the heapq module), the lowest valued entry is retrieved first.

# https://www.youtube.com/watch?v=f6RzBWu52W4&ab_channel=AnInsightfulTechie

# FIFO queue
q_fifo = queue.Queue(maxsize=10)
q_fifo.put(1)
q_fifo.put(2)
q_fifo.put(3)
print(q_fifo.get())
while not q_fifo.empty():
    print(q_fifo.get())

print("\n", "1== " * 20, "\n")

# LIFO queue
q_lifo = queue.LifoQueue(maxsize=5)
q_lifo.put(1)
q_lifo.put(2)
q_lifo.put(3)
print(q_lifo.get())
while not q_lifo.empty():
    print(q_lifo.get_nowait())


