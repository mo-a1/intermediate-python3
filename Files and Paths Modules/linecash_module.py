"""
The linecache module allows one to get any line from a Python source file, while attempting to optimize internally,
    using a cache, the common case where many lines are read from a single file. This is used by the traceback module
    to retrieve source lines for inclusion in the formatted traceback.
"""
import linecache

file = r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\linecash.txt"

line = linecache.getline(filename=file, lineno=10)

print(line)

linecache.checkcache(filename=file)
