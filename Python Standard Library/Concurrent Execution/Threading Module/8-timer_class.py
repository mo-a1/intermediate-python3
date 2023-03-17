import threading
from time import sleep

"""
Call a function after a specified number of seconds:
t = Timer(30.0, f, args=None, kwargs=None) t.start()
t.cancel() # stop the timer's action if it's still waiting
"""


def task():
    print("timer thread start")


my_timer = threading.Timer(interval=5, function=task)
my_timer.start()
# sleep(2)
# my_timer.cancel()
sleep(10)
