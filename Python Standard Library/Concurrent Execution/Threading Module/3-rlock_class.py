"""
The RLock (reentrant lock) class in the Python threading module is a subclass of the Lock class, which allows the same
 thread to acquire the lock multiple times without blocking. Here are the methods available in the RLock class:

__init__(self, /) - This method initializes a new reentrant lock object.

acquire(self, blocking=True, timeout=-1) -> bool - This method acquires the lock. If the lock is already held by the
 same thread, this method will increment the recursion level and return immediately. Otherwise, it behaves like the Lock
  class's acquire() method.

release(self) -> None - This method releases the lock. If the recursion level is greater than 1, it decrements the
 recursion level and returns immediately. Otherwise, it behaves like the Lock class's release() method.

__enter__(self) - This method is called when the lock is used as a context manager with the with statement. It acquires
 the lock.

__exit__(self, exc_type, exc_val, exc_tb) - This method is called when the with statement is exited. It releases the lock.

locked(self) -> bool - This method returns True if the lock is currently held by a thread, and False otherwise.

__repr__(self) -> str - This method returns a string representation of the reentrant lock object.

These are the main methods available in the RLock class. The RLock class also inherits the Lock class's locked() method
 and the Condition class's notify_all() and wait() methods.

It's important to note that while the RLock class provides more functionality than the Lock class, it is also more
complex to use correctly. In general, you should only use an RLock if you need to acquire a lock multiple times from
within the same thread. In most cases, a Lock or Semaphore is sufficient for synchronizing access to a shared resource.
"""

import threading

# Define a shared resource
shared_resource = []
rlock = threading.RLock()


# Define a function that adds items to the shared resource
def add_item(item):
    # If blocking is True (which is the default), the method will block until the lock is acquired.
    # If blocking is False, the method will return immediately, regardless of whether the lock was acquired or not.
    rlock.acquire()  # Acquire the RLock
    rlock.acquire()  # Acquire the RLock again
    shared_resource.append(item)
    rlock.release()  # Release the RLock
    rlock.release()  # Release the RLock again


# Define a function that removes items from the shared resource
def remove_item():
    rlock.acquire()  # Acquire the RLock
    if len(shared_resource) > 0:
        item = shared_resource.pop()
        rlock.release()  # Release the RLock
        return item
    else:
        rlock.release()  # Release the RLock
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

"""
In this example, we define a shared resource (a list) and an RLock object that will be used to synchronize access to
 the resource. We then define three functions:

add_item(item): This function adds an item to the shared resource. It first acquires the RLock twice (to demonstrate the
 reentrancy), adds the item to the resource, and then releases the RLock twice.

remove_item(): This function removes an item from the shared resource. It first acquires the RLock, checks if there are
 any items in the resource, removes the item if there is one, and then releases the RLock.

worker(): This function repeatedly adds and removes items from the shared resource. It calls add_item() to add an item
 to the resource, and then calls remove_item() to remove an item from the resource. It does this five times.

We then create two worker threads and start them. Each worker thread calls the worker() function, which repeatedly adds
 and removes items from the shared resource. Because the access to the shared resource is synchronized using an RLock,
  the same thread can acquire the lock multiple times without blocking.

Finally, we wait for the worker threads to complete and print the final state of the shared resource.
"""
