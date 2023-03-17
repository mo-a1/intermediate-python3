"""
The ThreadLocal class in the Python threading module provides a way to create thread-local data in a multi-threaded
 program. Thread-local data is data that is local to a specific thread and is not shared between threads. Here's some
  more information on the ThreadLocal class:

__init__(self) - This method initializes a new thread-local object.

get(self) - This method returns the value of the thread-local data for the current thread.

set(self, value) - This method sets the value of the thread-local data for the current thread.

hasattr(self) - This method returns True if the thread-local data has been set for the current thread, and False
otherwise.
"""

import threading

# Create a new thread-local object for the logger
local_logger = threading.local()


# Define a logger function that logs messages to the console
def log(message):
    # Get the logger for the current thread, or create a new one if it doesn't exist
    if not hasattr(local_logger, 'logger'):
        local_logger.logger = f"Thread {threading.current_thread().name} logger"
    # Log the message to the console
    print(f"{local_logger.logger}: {message}")


# Define a worker function that logs messages
def worker():
    log("Starting worker function")
    log("Working hard...")
    log("Finished worker function")


# Create several worker threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker)
    threads.append(t)

# Start the worker threads
for t in threads:
    t.start()

# Wait for the worker threads to finish
for t in threads:
    t.join()

print("Done")
