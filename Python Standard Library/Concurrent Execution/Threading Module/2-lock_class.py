"""
The Lock class is a synchronization primitive in the Python threading module that provides a way to lock access to a
 shared resource, allowing only one thread to access it at a time. Here are the methods available in the Lock class:

__init__(self, /) - This method initializes a new lock object.

acquire(self, blocking=True, timeout=-1) -> bool - This method acquires the lock. If the lock is already held by another
 thread, this method will block until the lock is released or until the optional timeout occurs.

release(self) -> None - This method releases the lock.

locked(self) -> bool - This method returns True if the lock is currently held by a thread, and False otherwise.

__enter__(self) - This method is called when the lock is used as a context manager with the with statement. It acquires
 the lock.

__exit__(self, exc_type, exc_val, exc_tb) - This method is called when the with statement is exited. It releases the
 lock.

These are the main methods available in the Lock class. The Lock class also provides a few other methods that are less
 commonly used, such as notify_all() and wait(), which are inherited from the threading.Condition class.

It's important to note that the Lock class is a low-level synchronization primitive, and it can be difficult to use
 correctly. In many cases, it's better to use a higher-level synchronization primitive, such as a threading.RLock or
  a threading.Semaphore, which provide additional functionality while still implementing the Lock interface.
"""

import threading

# Define a shared resource
shared_resource = []
lock = threading.Lock()


# Define a function that adds items to the shared resource
def add_item(item):
    lock.acquire()  # Acquire the lock
    shared_resource.append(item)
    lock.release()  # Release the lock


# Define a function that removes items from the shared resource
def remove_item():
    lock.acquire()  # Acquire the lock
    if len(shared_resource) > 0:
        item = shared_resource.pop()
        lock.release()  # Release the lock
        return item
    else:
        lock.release()  # Release the lock
        return None


# Define a function that repeatedly adds and removes items from the shared resource
def worker():
    for i in range(5):
        add_item(i)
        print(f"Added item {i}")
        item = remove_item()
        if item is not None:
            print(f"Removed item {item}")
        else:
            print("No items left")


# Create two worker threads
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

# Start the worker threads
t1.start()
t2.start()

# Wait for the worker threads to complete
t1.join()
t2.join()

# Print the final state of the shared resource
print(f"Final state of shared resource: {shared_resource}")
