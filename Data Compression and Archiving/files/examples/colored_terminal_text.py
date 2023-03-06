import datetime
from contextlib import contextmanager, ExitStack, suppress, redirect_stdout


@contextmanager
def red_text():
    print("\u001b[31m")
    yield
    print("\u001b[0m")


@contextmanager
def yellow_text():
    print("\u001b[33m")
    yield
    print("\u001b[0m")


@contextmanager
def time_now():
    print(datetime.datetime.now())
    yield


with red_text():
    print("i am red")

print("return to default")

with yellow_text():
    print("i am yellow")

print("return to default")

with ExitStack() as stack:
    stack.enter_context(redirect_stdout(open("output.txt", "w")))
    stack.enter_context(red_text())
    stack.enter_context(time_now())
    stack.enter_context(suppress(ZeroDivisionError))
    print("hello")
    print("color still exist because context manager not exit yet")
    print(1/0)

print("here i am normal")
