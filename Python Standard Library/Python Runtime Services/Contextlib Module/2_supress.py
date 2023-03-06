from contextlib import suppress
import os

# try:
#     os.remove("temp.txt")
# except FileNotFoundError:
#     pass


# can replace try except statements
with suppress(FileNotFoundError):
    os.remove("temp.txt")
