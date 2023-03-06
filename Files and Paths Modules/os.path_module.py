import os.path as op
from datetime import datetime

path = r"../Contextlib Module"
fpath = r"D:\Programing\Learning\Code\python3\intermediate-python3\Files and Paths Modules\testes\linecash.txt"
print(op.basename(path))
print(op.isdir(path))
print(op.dirname(path))
print(op.exists(path))
print("--------------------- 1 ---------------------")
print(op.split(fpath)[1])
print(op.splitext(fpath)[1])
print(op.abspath(fpath))
print(op.getsize(fpath) / 1024, "kb")

# Return the time of last modification of path. The return value is a floating point number
print(datetime.fromtimestamp(op.getmtime(fpath)))

# Return the time of last access of path. The return value is a floating point number
print(datetime.fromtimestamp(op.getatime(fpath)))
