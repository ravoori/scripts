from functools import total_ordering
from collections import deque
from itertools import chain
import bisect
@total_ordering
class zz(object):
    def __init__(self, val, key_func):
        self.__val = val
        self.__key_func = key_func
    def __str__(self):
        return str(self.__val)
    def __repr__(self):
        return repr(self.__val)
    def __lt__(self, other):
        return self.__key_func(self.__val) < self.__key_func(other.__val) if self.__key_func else self.__val < other.__val
    def __eq__(self, other):
        return self.__key_func(self.__val) == self.__key_func(other.__val) if self.__key_func else self.__val == other.__val

def print_highest_n(l, key_func=None, n=5):
    it = (zz(x, key_func) for x in l)
    d = deque(maxlen=n+1)
    for el in it:
        bisect.insort(d, el)
        if len(d) == d.maxlen:
            d.popleft()
        print("\x1b[2J\x1b[H")
        print(*d)
