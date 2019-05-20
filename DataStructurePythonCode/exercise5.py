# -*-coding:utf-8-*-
# !/usr/bin/env python
# Copyright 2018 .All Rights Reserved.
# Author: Jie, memdreams@gmail.com
# exercise5.py 2018-08-17
import sys

# R 5.1
def solution1(n):
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)

# R 5.2
def solution2(n):
    data = []
    a = sys.getsizeof(data)
    for k in range(n):
        b = sys.getsizeof(data)
        if a < b:
            a = b
            print('Size in bytes changed at: {:4d}'.format(k-1))
        data.append(None)

# R 5.3
def solution3(n):
    data = [None for _ in range(n)]

    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.pop()

# R 5.4
import ctypes  # provides low-level arrays

class DynamicArray(object):
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not -self._n <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):  # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation
    
    
# C-5.13
def solution13(n, length=6):
    data = [0 for _ in range(length)]
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)

# C-5.14
from random import randrange
def shuffle(l):
    n = len(l)
    result = [None for _ in range(n)]
    for i in range(n):
        item = l.pop()
        r = randrange(n)
        while result[r]:
            r = randrange(n)
        result[r] = item

    return result



if __name__ == '__main__':
    # for i in range(10):
    #     c = 1 + i
    #
    #
    # n = 127
    # a = DynamicArray()
    #
    # l = [i for i in range(10)]
    # print(shuffle(l))
    d = {}
    d['darkblueSwDress']= 159.8
    d['blackLongSkirt'] = 199.8
    d['greyHighCollarSw'] = 79
    d['brownLowCollarSw'] = 99.8
    d['blackLongSleeveT'] = 125.8
    d['blackShortSleevesT'] = 62.8
    d['blaclShortSkirt'] = 159.84
    d['pinkShortDress'] = 93.4
    d['blueShortT'] = 199
    d['noSleeveLongDress'] = 489
    # d['summerNiuzaiqun'] = 80.8
    d['whiteT'] = 53.8
    d['eggwhiteDress'] = 279.8
    d['coulorfulSkirt'] = 229.8
    item1 = sum([d['noSleeveLongDress'], d['blackLongSkirt'], d['blueShortT'], d['blaclShortSkirt']] )
    print(item1)
    item2 = sum([d['coulorfulSkirt'], d['eggwhiteDress'], d['blackLongSleeveT'], d['brownLowCollarSw']])
    item3 = 79+93.4+62.8+53.8

    print(item1 + item2 -50)

    updown = {}
    updown['yellowSw'] = 160


