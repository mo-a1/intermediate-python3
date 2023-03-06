import pathlib

print("-------------------  class: PureWindowsPath  --------------------")

path = r"C:\Users\20106\PycharmProjects\intermediate-python3\Contextlib Module\2_supress.py"

a = pathlib.PureWindowsPath(path)   # <class 'pathlib.PureWindowsPath'>

# ----------- attributes --------------

print(a)             # C:\Users\20106\PycharmProjects\intermediate-python3\Contextlib Module\2_supress.py
print(a.parts)       # ('C:\\', 'Users', '20106', 'PycharmProjects', 'intermediate-python3', 'Contextlib Module', '2_supress.py')
print(a.drive)       # C:
print(a.anchor)      # C:\
print(a.parent)      # C:\Users\20106\PycharmProjects\intermediate-python3\Contextlib Module
print(a.parents)     # <PureWindowsPath.parents>
print(a.name)        # 2_supress.py
print(a.stem)        # 2_supress
print(a.suffix)      # .py

# -------- checks ---------

print(a.is_absolute())  # True
print(a.match("*.py"))  # True
b = pathlib.PureWindowsPath(r"/Contextlib Module/2_supress.py")
print(b.is_relative_to("/Contextlib Module"))   # True

# ------- edits ------------ :: return -> pathlib.PureWindowsPath object

print(a.with_name("test.txt"))   # C:\Users\20106\PycharmProjects\intermediate-python3\Contextlib Module\test.txt
print(a.with_stem("stem"))       # C:\Users\20106\PycharmProjects\intermediate-python3\Contextlib Module\stem.py
print(a.with_suffix(".zip"))     # C:\Users\20106\PycharmProjects\intermediate-python3\Contextlib Module\2_supress.zip
