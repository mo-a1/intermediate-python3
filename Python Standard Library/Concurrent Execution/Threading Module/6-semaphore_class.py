"""
The Semaphore class in the Python threading module provides a way to restrict the number of threads that can access a
shared resource at the same time. Here's some more information on the Semaphore class:

__init__(self, value=1) - This method initializes a new semaphore object with an initial value. The value indicates the
maximum number of threads that can access the shared resource at the same time.

acquire(self, blocking=True, timeout=None) - This method acquires the semaphore. If the semaphore is already held by the
 maximum number of threads, the method will block until it is released. If the blocking parameter is set to False, the
 method will return immediately with a value of False if the semaphore cannot be acquired. If a timeout value is
 specified, the method will wait for the specified amount of time before returning.

release(self) - This method releases the semaphore, allowing other threads to acquire it.

"""
import random
import threading
from time import sleep

# https://superfastpython.com/thread-semaphore/#Need_for_a_Semaphore


semaphore = threading.Semaphore(1)


# each time the semaphore is acquired, the internal counter is decremented. Each time the semaphore is released,
# the internal counter is incremented. The semaphore cannot be acquired if the semaphore has no available positions
# in which case, threads attempting to acquire it must block until a position becomes available.

# we use it to control how many thread can run in parallel


def task(thread_name):
    for i in range(11):
        sleep(1)
        print(f"{thread_name} -- {i}   ")


t1 = threading.Thread(target=task, args=("t1",))
t2 = threading.Thread(target=task, args=("t2",))
t3 = threading.Thread(target=task, args=("t3",))

# semaphore.acquire()
# t1.start()
# t2.start()
# semaphore.acquire(blocking=True, timeout=5)
# sleep(2)

# semaphore.release(1)
# t3.start()


print("############# use semaphore with as a context manager to auto release places in semaphore #############")


def test(semaphore_, number):
    value = random.randint(1, 5)
    # attempt to acquire a semaphore
    with semaphore_:
        sleep(value)
        print(f"Thread number: {number} got value = {value} ")


my_semaphore = threading.Semaphore(3)
for i in range(5):
    t = threading.Thread(target=test, args=(my_semaphore, i))
    t.start()


