class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        n = self.start
        while n < self.end:
            yield n
            n += 1

    def __reversed__(self):
        n = self.end
        while n > self.start:
            yield n
            n -= 1


for i in Counter(1, 10):
    print(i)

print("## 1 " * 20)

for i in reversed(Counter(1, 10)):
    print(i)

