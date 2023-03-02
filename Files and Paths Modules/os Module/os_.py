import os
from contextlib import suppress, redirect_stdout

# https://www.youtube.com/watch?v=tJxcKyFMTGo&ab_channel=CoreySchafer

path = r"/Numbers"

# current work directory
cwd = os.getcwd()

os.chdir(path)

print(os.getcwd())

os.chdir(cwd)
print(os.getcwd())

# list of files on dir.
print(os.listdir(path))

# make directories
with suppress(FileExistsError):
    os.mkdir("by mkdir")
    os.makedirs("by_makedirs/sub_dir")

# remove directories
os.rmdir("by mkdir")
os.removedirs("by_makedirs/sub_dir")

# rename files
with suppress(FileNotFoundError):
    os.rename("rename.html", "renamedd.html")

# file details
print(os.stat(path))    # -> like named tuple
print(os.stat(path)[0])
print(os.stat(path).st_ctime)   # -> time stamp

# os.walk()
with redirect_stdout(open("os_walk.txt", "w")):
    for dirpath, dirname, filename in os.walk(r"/"):
        if ".git" in dirpath:
            continue
        print("dir_path:", dirpath)
        print("dir_name:", dirname)
        print("file_name:", filename)
        print("-" * 30)

with redirect_stdout(open("os functions.txt", "w")):
    print(help(os))
