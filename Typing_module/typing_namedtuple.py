import typing


class Point2D(typing.NamedTuple):
    x: int = 0
    y: int = 0


start = Point2D(10, 15)
print(start)
print(start.__annotations__)
