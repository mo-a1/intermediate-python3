import zipfile
import shutil

# make a zip file without compression
with zipfile.ZipFile("new.zip", mode="w") as writer:
    writer.write("1_file.css")
    writer.write("1a_file.html")

# make a zip file with compression
with zipfile.ZipFile("new2.zip", mode="w", compression=zipfile.ZIP_DEFLATED) as writer:
    writer.write("1_file.css")
    writer.write("1a_file.html")


# extract files
with zipfile.ZipFile("new2.zip", "r") as zfile:
    zfile.extract("1_file.css", "files")
    zfile.extractall("files")

    # ################### methods #################### #

    print(zfile.namelist())   # ['1_file.css', '1a_file.html']
    print(zfile.testzip())
    print(zfile.setpassword(bytes(123)))
    print(zfile.infolist())


# this will archive only the directory without its contents
with zipfile.ZipFile("new3.zip", "w") as arch:
    arch.write("files")

# this will archive the directory and its contents
shutil.make_archive("new4", "zip", "../Python Runtime Services/Contextlib Module")
shutil.unpack_archive("new4.zip", "files")
