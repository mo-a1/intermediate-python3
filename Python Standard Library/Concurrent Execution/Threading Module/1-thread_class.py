from threading import Thread
from time import sleep
from coloring import green_text, red_text

"""
The Thread class is a fundamental class in the Python threading module, and it represents an individual thread of
 control in a program. It allows you to create and manage threads in a Python program. Here are some of the important
  methods available in the Thread class:

__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None) - This method initializes a
 new thread object. It takes several optional arguments, including the target function to be run in the new thread,
  the name of the thread, and any arguments to be passed to the target function.

start(self) - This method starts the thread's activity. It invokes the target function in a new thread.

run(self) - This method is the entry point for the thread. It is called when the thread is started and it runs the
 target function.

join(self, timeout=None) - This method blocks the calling thread until the thread whose join() method is called
 completes or until the optional timeout occurs.

is_alive(self) - This method returns True if the thread is alive, which means it has been started and has not yet
 completed.

getName(self) - This method returns the name of the thread.

setName(self, name) - This method sets the name of the thread.

ident - This read-only attribute returns the thread's identifier.

daemon - This attribute is a boolean that indicates whether the thread is a daemon thread.

These are just a few examples of the methods available in the Thread class. The Thread class also provides other methods
 and attributes for managing threads, such as enumerate(), setDaemon(), isDaemon(), and is_alive().
"""


# https://realpython.com/intro-to-python-threading/
# https://superfastpython.com/learning-paths/#Threading_Learning_Path

def count(thread_name, num):
    with green_text():
        print(thread_name, "start")
    while num > 0:
        print(f"{thread_name} -> {num}   ")
        sleep(1)
        num -= 1
    with red_text():
        print(thread_name, "end")


# start a thread
t1 = Thread(target=count, args=("thread1", 10,))
t2 = Thread(target=count, args=("thread2", 10,))
# t1.start()
# t2.start()

# join: used to prevent other threads from execution till this thread end
t1.start()
t1.join()
t2.start()

# demon thread: if the program reach the end of code then the demon thread will stop.
d_thr = Thread(target=count, args=("daemon_thread", 15,), daemon=True)
d_thr.start()

print("MAIN THREAD")
