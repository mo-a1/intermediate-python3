from threading import Thread
from time import sleep
from coloring import green_text, red_text


# https://realpython.com/intro-to-python-threading/


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
# t1.join()
t2.start()

# demon thread: if the program reach the end of code then the demon thread will stop.
d_thr = Thread(target=count, args=("daemon_thread", 15,), daemon=True)
d_thr.start()
d_thr.join()
sleep(2)

print("MAIN THREAD")
