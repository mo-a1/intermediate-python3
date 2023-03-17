"""
The Timer class in the Python threading module provides a way to schedule a function to be called after a specified
    amount of time has elapsed. Here are the methods provided by the Timer class:

__init__(self, interval, function, args=None, kwargs=None) - This method initializes a new timer object. The interval
    parameter specifies the time interval in seconds before the function will be called. The function parameter is the
    function that will be called when the timer expires. The args and kwargs parameters are optional arguments that will
    be passed to the function when it is called.

start(self) - This method starts the timer. The function will be called after the specified interval has elapsed.

cancel(self) - This method cancels the timer. The function will not be called if the timer has been cancelled.

is_alive(self) - This method returns True if the timer is still running, and False otherwise.
"""

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
