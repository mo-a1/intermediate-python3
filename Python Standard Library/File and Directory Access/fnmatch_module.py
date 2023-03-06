import os
import fnmatch

# methods: fnmatch, filter, translate

for file in os.listdir(r""):
    if fnmatch.fnmatch(file, "*.py"):
        print(file)

files = [f for f in os.listdir("../Python Runtime Services/Contextlib Module")]

print(fnmatch.filter(files, "*.txt"))   # list

regex = fnmatch.translate("11.txt")   # str: regex pattern
print(regex)
