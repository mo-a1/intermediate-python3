import os
import fnmatch

# methods: fnmatch, filter, translate

for file in os.listdir(r"D:\Programing\Learning\Code\python3\intermediate-python3\Python Standard Library\File and Directory Access"):
    if fnmatch.fnmatch(file, "*.py"):
        print(file)

files = [f for f in os.listdir("../Python Runtime Services/Contextlib Module")]

print(fnmatch.filter(files, "*.txt"))   # list

regex = fnmatch.translate("11.txt")   # str: regex pattern
print(regex)
