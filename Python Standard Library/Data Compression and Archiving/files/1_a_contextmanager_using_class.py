
class open_file:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with open_file(file_name="using_class.txt", mode="w") as f:
    f.write("hello")

print(f.closed)
