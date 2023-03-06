import pickle
import shelve

with open("pickle_out.pickle", "rb") as pk:
     a = pickle.load(pk)
     print(a)