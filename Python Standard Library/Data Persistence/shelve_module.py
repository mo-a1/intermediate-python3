"""
    A “shelf” is a persistent, dictionary-like object. The difference with “dbm” databases is that the values
(not the keys!) in a shelf can be essentially arbitrary Python objects — anything that the pickle module can handle.
This includes most class instances, recursive data types, and objects containing lots of shared sub-objects.
The keys are ordinary strings.
"""
import shelve

my_dict = {1: 2, 2: 4, 4: 8}


class DataEntry:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def sum_(self):
        return self.start + self.end, "sum_"


my_obj = DataEntry(5, 5)

# ################# shelve.open() ################## #
with shelve.open("shelved_data.db") as db:
    db["adict"] = my_dict
    db["aobj"] = my_obj
