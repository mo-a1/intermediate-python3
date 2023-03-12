import logging
from typing import List
from itertools import accumulate
import basics

logging.basicConfig(filename="e-logs.log", filemode="w", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s - %(funcName)s")


class Calcs:
    def __init__(self, values: List[int]):
        self.values = values

    def sum(self):
        if len(self.values) < 2:
            logging.warning("only one value exist")
        return sum(self.values)

    def accumulator(self):
        if self.sum() > 100:
            logging.warning("big value")
        return accumulate(self.values)

    def checker(self):
        m = min(self.values)
        if m < 0:
            logging.error(f"there are negative value (values) min -> {m}")
        else:
            return True

    def z_checker(self):
        log = False
        for i in self.values:
            try:
                max(self.values) / i
            except ZeroDivisionError:
                if not log:
                    logging.exception("ZeroDivisionError")
                    log = True
                else:
                    pass


try_ = Calcs([1, 5, 9, 11, 259, -5, -9, 0, 0, 66])
print(try_.sum())
print(try_.accumulator())
print(try_.checker())
print(try_.z_checker())

try_ = Calcs([1])
print(try_.sum())
print(try_.accumulator())
print(try_.checker())
print(try_.z_checker())
