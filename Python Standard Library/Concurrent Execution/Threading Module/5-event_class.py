"""
The Event class in the Python threading module provides a simple way for threads to signal each other about the
 occurrence of an event. Here's some more information on the Event class:

__init__(self, /) - This method initializes a new event object.

is_set(self) - This method returns True if the event is set, and False otherwise.

set(self) - This method sets the event, indicating that it has occurred. Any threads that are waiting for the event to
 occur will be notified.

clear(self) - This method clears the event, indicating that it has not occurred. Any threads that are waiting for the
 event to occur will continue to wait.

wait(self, timeout=None) - This method waits for the event to occur. If the event is already set, the method returns
 immediately. If the event is not set, the method will block until the event is set or a timeout occurs. If a timeout
  value is specified, the method will wait for the specified amount of time before returning.
"""

import threading
import time

# Create a new event object
event = threading.Event()


# Define a worker function that waits for the event to occur
def worker():
    print("Worker waiting for event to occur")
    event.wait()
    print("Worker continuing after event occurred")


# Create a new thread to run the worker function
thread = threading.Thread(target=worker)

# Start the worker thread
thread.start()

# Wait for some time
print("Main thread waiting for some time")
time.sleep(2)

# Set the event, indicating that it has occurred
print("Main thread setting event")
event.set()

# Wait for the worker thread to finish
thread.join()

print("Done")
