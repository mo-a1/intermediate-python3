from functools import lru_cache, cache
from urllib import request, error


@lru_cache(maxsize=32)
def get_pep(num):
    """ Retrieve text of a Python Enhancement Proposal """
    resource = 'https://peps.python.org/pep-%04d/' % num
    try:
        with request.urlopen(resource) as s:
            return s.read()
    except error.HTTPError:
        return 'Not Found'


@cache
def fib_num(n):
    if n < 2:
        return n
    else:
        return fib_num(n-1) + fib_num(n-2)


if __name__ == '__main__':
    for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))
    print(get_pep.cache_info())
    print(fib_num(10))
    print(fib_num(11))
    print(fib_num.cache_info())
