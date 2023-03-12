from enum import Enum, auto, unique


class ConnectionState(Enum):
    CLOSED = 0
    WAITING = 1
    OPENED = 2
    TIME_OUT = 3


inp = int(input("what state: "))
if ConnectionState(inp) is ConnectionState.CLOSED:
    print("connection closed")


# use auto values starts from 1
class UserState(Enum):
    ADMIN = auto()
    USER = auto()
    BLOCKED_USER = auto()


# force using unique values
@unique
class GameResult(Enum):     # raise ValueError('duplicate values found in %r: %s'
    EXIT = 0                # ValueError: duplicate values found in <enum 'GameResult'>: PAUSE -> EXIT
    PAUSE = 0
    BREAK = 2
