from contextlib import ExitStack, contextmanager


@contextmanager
def red_text():
    print("\u001b[31m")
    yield
    print("\u001b[0m")


text_files = ["using_class.txt", "using_func.txt"]
# text_files = ["using_class.txt", "using_func.txt", "temp.txt"]

with ExitStack() as stack:
    # stack.enter_context(suppress(FileNotFoundError))
    files = [stack.enter_context(open(file, "r")) for file in text_files]
    stack.enter_context(red_text())
    print(files, type(files))
    for f1_line, f2_line in zip(files[0], files[1]):
        print(f1_line.rstrip())
        print(f2_line.rstrip())

print(help(ExitStack))
