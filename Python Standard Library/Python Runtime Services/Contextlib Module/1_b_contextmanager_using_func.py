from contextlib import contextmanager


@contextmanager
def open_file(file_name, mode):
    f = open(file_name, mode)
    try:
        yield f
    finally:
        print("file closed")
        f.close()


with open_file("using_func.txt", "w") as file:
    file.write("hello from func")

print(file.closed)
