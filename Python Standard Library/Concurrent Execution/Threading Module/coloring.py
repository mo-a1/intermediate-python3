from contextlib import contextmanager


@contextmanager
def red_text():
    print("\u001b[31m")
    yield
    print("\u001b[0m")


@contextmanager
def green_text():
    print("\u001b[32m")
    yield
    print("\u001b[0m")
