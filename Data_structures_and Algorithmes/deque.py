from collections import deque
import random
import queue

f_names = ['ali ', 'mazen ', 'mahmoud ', 'othman ', 'mohamed ', 'kareem ', 'nora ', 'amany ', 'hala ', 'aya ']
other_names = ['ashraf ', 'ahmed ', 'sayed ', 'tarek ', 'abelazzez ', 'mroan ', 'khaled ', 'ali ', 'mazen ',
               'mahmoud ', 'othman ', 'mohamed ', 'kareem ']


def generate_names(names_num: int) -> str:
    for i in range(names_num):
        yield random.choice(f_names).capitalize() + random.choice(other_names).capitalize() + \
              random.choice(other_names).capitalize()


def names_filter(pattern: str, num: int) -> deque:
    result = deque([], maxlen=num)
    for name in generate_names(100):
        if name.startswith(pattern):
            result.append(name)
    return result


print(names_filter("M", 5))

print('*1' * 20)

q = queue.Queue(maxsize=3)
q.put(10, block=False)
q.put(20, block=False)
q.put(30, block=False)

print(q.get())
print(q.get())
print(q.get())
# print(q.get_nowait())
print(q.empty())
print(q.full())
q.put_nowait(40)
print(q.queue)
