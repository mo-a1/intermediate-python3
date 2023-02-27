from contextlib import redirect_stdout

with redirect_stdout(open("output.txt", "w")):
    print("hello from redirect_stdout context manager.")
    print(redirect_stdout.__doc__)

