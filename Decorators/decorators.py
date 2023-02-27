import time
from functools import wraps


def decorator_func(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")

    return wrapper_func


@decorator_func
def add(x, y):
    print(x + y)


add(x=2, y=3)
print(add.__name__)  # because of using @wraps decorator


def timing(func):
    @wraps(func)
    def wrapper():
        start_t = time.time()
        func()
        end_t = time.time()
        print(f"Executed in {end_t - start_t} sec")

    return wrapper


@timing
def loop():
    b = 0
    for i in range(100000):
        b += i
    return b


loop()


def loop_2():
    b = 0
    for i in range(100000):
        b += i
    return b


func_ = timing(loop_2)
func_()
