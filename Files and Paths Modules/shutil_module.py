import shutil
import os

# ########################## [ copy methods ] ############################ #

# 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'

src = r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\test_1\11df.py"
dst = r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\test_2"

# shutil.copyfile(src, dst)   # copy file only.
# shutil.copy(src, dst)       # copy the file and its permissions
# shutil.copy2(src, dst)      # copy the file and its metadata
# shutil.copymode(src, dst)   # only copy the permissions from src to dst
# shutil.copystat(src, dst)   # only copy the metadata from src to dst
# shutil.copytree(src, dst)   # copy contents of directory (src) to anew directory its path and name = (dst) which will
#                               be created and Error raised if dir already found


# os.remove(r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\test_2\11df.py")

print([f for f in dir(shutil) if "_" and "Error" not in f])

print(shutil.disk_usage(src).total/1024/1024/1024)
