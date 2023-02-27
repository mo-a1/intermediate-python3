import fnmatch
import os

# .filter()
file_filter = [file for file in fnmatch.filter(os.listdir(r"C:\Users\20106\Downloads"), '*.exe')]
print(file_filter)

# .fnmatchcase()
file_filter = [file for file in os.listdir(r"C:\Users\20106\Downloads") if fnmatch.fnmatchcase(file, '*Desk*')]
print(file_filter)
