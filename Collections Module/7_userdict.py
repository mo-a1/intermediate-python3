from collections import UserDict


class UDict(UserDict):
    def pop(self, ele=None):
        raise TypeError("Not Allowed")

    def _del_(self):
        raise TypeError("“Not Allowed”")

    def popitem(self, ele=None):
        raise TypeError("“Not Allowed”")


uDic = UDict({1: 1, 4: 2, 16: 4})
uDic[25] = 4

print(uDic)
