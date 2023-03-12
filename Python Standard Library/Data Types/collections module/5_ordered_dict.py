from collections import OrderedDict

dict_ = {
    "a": 1,
    "b": 2
}
o_dict = OrderedDict(dict_)
print(dict_)

# .popitem(last=True)
#  popitem() method for ordered dictionaries returns and removes a
#       (key, value) pair. The pairs are returned in LIFO order if
#       last is true or FIFO order if false.

print(o_dict.popitem(last=False))
