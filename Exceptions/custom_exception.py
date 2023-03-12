class AnException(Exception):
    """ Raise when x exception raises """


class AnyException(Exception):
    pass


class MyCustomException(Exception):
    def __init__(self):
        self.msg = 'Message about my error'

    def __str__(self):
        return repr(self.msg)


class MyException(Exception):
    def __init__(self, arg1=None, arg2=None):
        super().__init__()
        self.msg = 'Message about my error'
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return repr(self.msg)


# raise MyException


