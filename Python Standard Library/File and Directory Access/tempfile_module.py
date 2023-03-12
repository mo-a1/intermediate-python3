"""
    This module creates temporary files and directories. It works on all supported platforms. TemporaryFile,
NamedTemporaryFile, TemporaryDirectory, and SpooledTemporaryFile are high-level interfaces which provide
automatic cleanup and can be used as context managers. mkstemp() and mkdtemp() are lower-level functions
which require manual cleanup.
"""
import tempfile
import os

path = r"D:\Programing\Learning\Code\python3\intermediate-python3\Python Standard Library\File and Directory Access\testes"

print("---------------- TemporaryFile ----------------")

# does not appear in Windows explorer
with tempfile.TemporaryFile(mode="w+t", dir=path, delete=True) as tfile:
    print(tfile.name)
    tfile.write("hello from TemporaryFile")
    tfile.seek(0)
    print(tfile.readline())

print("---------------- NamedTemporaryFile ----------------")

with tempfile.NamedTemporaryFile(mode="w+t", dir=path, prefix="prefix", suffix="suffix", delete=True) as ntfile:
    ntfile.write("hello from NamedTemporaryFile ")
    print(ntfile.name)
    print(os.listdir(path))

print("---------------- TemporaryDirectory ----------------")

with tempfile.TemporaryDirectory(suffix="suffix", prefix="prefix", dir=path) as tdir:
    open(file=f"{tdir}\\test.txt", mode="w")
    print(tdir)
    print("tdire is dire? ", os.path.isdir(tdir))
    print(os.listdir(tdir))

print("---------------- mkdtemp() ----------------")

# dir does not deleted
# default dir is Temp dir on system

out_dir = tempfile.mkdtemp(suffix="suffix", prefix="prefix", dir=path)
print(out_dir)

print("---------------- mkstemp() ----------------")

# creates temporary file
# temp file is does not delete

out_file = tempfile.mkstemp(dir=path)
print(out_file)
