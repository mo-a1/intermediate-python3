from contextlib import contextmanager
import pprint
import os


@contextmanager
def change_cwd(destination):
    cwd = os.getcwd()
    try:
        os.chdir(destination)
        yield os.listdir()
    finally:
        os.chdir(cwd)


path_1 = r"C:\Users\20106\PycharmProjects\Advanced python\Data_structures_and Algorithmes"
path_2 = r"C:\Users\20106\PycharmProjects\Advanced python\Collections Module"

with change_cwd(path_1) as files:
    pprint.pprint(files)

print(os.getcwd())

with change_cwd(path_2) as files:
    pprint.pprint(files)
