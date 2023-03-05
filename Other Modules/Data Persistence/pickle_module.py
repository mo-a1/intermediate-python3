import pickle

# it can store an object with its status and values on a file in bytes format then we can get this object.
# it is useful with objects which getting it need alot of processing or query a database.
# https://www.youtube.com/watch?v=2Tw39kZIbhs&ab_channel=sentdex
# https://www.youtube.com/watch?v=XzkhtWYYojg&ab_channel=RealPython


class DataEntry:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def sum_(self):
        return self.start + self.end, "sum_"


de = DataEntry(11, 22)

with open("pickle_out.pickle", "wb") as pickle_out:
    pickle.dump(de, pickle_out)

with open("pickle_out.pickle", "rb") as pickle_in:
    pickled_obj = pickle.load(pickle_in)
    print(pickled_obj.sum_())
