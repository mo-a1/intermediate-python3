from contextlib import redirect_stdout

with open("output.txt", "w") as output:
    with redirect_stdout(output):
        print("hello from redirect_stdout context manager.")
        print(redirect_stdout.__doc__)

