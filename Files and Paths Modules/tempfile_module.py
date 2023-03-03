import tempfile
import os
import time

path = r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes"

print("---------------- TemporaryFile ----------------")

with tempfile.TemporaryFile(mode="w+t", dir=path, delete=True) as tfile:
    print(tfile.name)
    tfile.write("hello from TemporaryFile")
    tfile.seek(0)
    print(tfile.readline())

print("---------------- NamedTemporaryFile ----------------")

with tempfile.NamedTemporaryFile(mode="w+t", dir=path, prefix="prefix", suffix="suffix", delete=True) as ntfile:
    ntfile.write("hello from NamedTemporaryFile ")
    print(os.listdir(path))

print("---------------- TemporaryDirectory ----------------")

with tempfile.TemporaryDirectory(suffix="suffix", prefix="prefix", dir=path) as tdir:
    open(file=f"{tdir}\\test.txt", mode="w")
    print(tdir)
    print("tdire is dire? ", os.path.isdir(tdir))
    print(os.listdir(tdir))
    # time.sleep(30)

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
