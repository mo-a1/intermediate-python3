"""
The Barrier class in the Python threading module provides several methods for synchronizing the execution of multiple
 threads. Here are the methods provided by the Barrier class:

__init__(self, parties, action=None, timeout=None) - This method initializes a new barrier object. The parties parameter
 indicates the number of threads that are expected to wait at the barrier. The action parameter is a callable object
 that will be called when all the threads have reached the barrier. The timeout parameter is an optional timeout value
 in seconds.

wait(self, timeout=None) - This method waits for all the threads to reach the barrier. If the barrier has not been
 reached by all the threads, the method will block until it is reached or a timeout occurs. If a timeout value is
 specified, the method will wait for the specified amount of time before returning.

reset(self) - This method resets the barrier to its initial state, allowing the threads to wait at the barrier again.

abort(self) - This method raises a BrokenBarrierError in all the waiting threads, causing them to exit with an exception

n_waiting(self) - This method returns the number of threads that are currently waiting at the barrier.

parties(self) - This method returns the number of threads that are expected to wait at the barrier.

broken(self) - This method returns True if the barrier has been broken, and False otherwise.
"""

# https://superfastpython.com/thread-barrier-in-python/
# https://en.wikipedia.org/wiki/Barrier_(computer_science)

import threading

# Create a new barrier object for 3 threads
barrier = threading.Barrier(3)


# Define a worker function that waits at the barrier
def worker():
    print("Worker before barrier")
    barrier.wait(5)
    print("Worker after barrier")


# Create several worker threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker)
    threads.append(t)

# Start the worker threads
for t in threads:
    t.start()

# Wait for the worker threads to reach the barrier
print("Waiting for all threads to reach the barrier")
barrier.wait()
print("All threads have reached the barrier")

# Check the state of the barrier
print("Number of waiting threads:", barrier.n_waiting)
print("Expected number of threads:", barrier.parties)
print("Barrier is broken:", barrier.broken)

# Reset the barrier
barrier.reset()

# Start the worker threads again
print("Starting the worker threads again")
for t in threads:
    t.start()

# Wait for the worker threads to finish
for t in threads:
    t.join()

print("Done")
