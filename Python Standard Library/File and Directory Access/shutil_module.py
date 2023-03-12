import shutil

# ########################## [ copy and move methods ] ############################ #

# 'copy', 'copy2', 'copyfile', 'copymode', 'copystat', 'copytree, 'move'

src = r"testes\test_1\11df.py"
dst = r"testes\test_2"

# shutil.copyfile(src, dst)   # copy file only.
# shutil.copy(src, dst)       # copy the file and its permissions
# shutil.copy2(src, dst)      # copy the file and its metadata
# shutil.copymode(src, dst)   # only copy the permissions from src to dst
# shutil.copystat(src, dst)   # only copy the metadata from src to dst
# shutil.copytree(src, dst)   # copy contents of directory (src) to anew directory its path and name = (dst) which will
#                               be created and Error raised if dir already found
# shutil.move(src, dst, copy_function=shutil.copy)  # move file from dist to src following the copy function

# --------- shutil.move(src, dst, copy_function=copy2) --------
# Recursively move a file or directory (src) to another location (dst) and return the destination.
# If the destination is an existing directory, then src is moved inside that directory. If the destination already
# exists but is not a directory, it may be overwritten depending on os.rename() semantics.


# os.remove(r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\test_2\11df.py")

print([f for f in dir(shutil) if "_" and "Error" not in f])

print(shutil.disk_usage(src).total/1024/1024/1024)
