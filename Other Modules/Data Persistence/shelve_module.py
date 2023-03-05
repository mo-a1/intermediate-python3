import shelve

my_dict = {1: 2, 2: 4, 4: 8}


class DataEntry:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def sum_(self):
        return self.start + self.end, "sum_"


my_obj = DataEntry(5, 5)

with shelve.open("shelved_data", protocol=5) as db:
    db["adict"] = my_dict
    db["aobj"] = my_obj
