import os
import fnmatch

# methods: fnmatch, filter, translate

for file in os.listdir(r"../Files and Paths Modules"):
    if fnmatch.fnmatch(file, "*.py"):
        print(file)

files = [f for f in os.listdir("../Contextlib Module")]

print(fnmatch.filter(files, "*.txt"))

regex = fnmatch.translate("11.txt")
print(regex)

