"""
<Data Structure and Algorithms in Python> Chapter 2

Date: 2018.03.15
Author: Jie
"""

# Test Decorators
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func

@deco
def myfunc():
    print(" myfunc() called.")

# myfunc = deco(myfunc) # is the same as @deco, only one of them can exist

# myfunc()  # only be decorated once
# myfunc()

# 使用内嵌包装函数确保每次myfunc1都被decorator调用
def deco1(func):
    def _deco():
        print("before myfunc1() called.")
        func()
        print("  after myfunc1() called.")
    return _deco # notice return _deco, not func

@deco1
def myfunc1():
    print(" myfunc1() called.")
    return 'OK'

# myfunc1 = deco1(myfunc1) # is the same as @deco1, only one of them can exist

# myfunc1()
# myfunc1()


import cProfile # cProfile.run('testfunc()') is used for test the running time of the function


# R-2.4
class Flower(object):
    def __init__(self, name='flower', petal=5, price=5.0):
        self._name = name
        self._petal = petal
        self._price = price

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, val):
        self._name = val

    @property
    def petal(self):
        return self._petal
    @petal.setter
    def petal(self, val):
        self._petal = val

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, val):
        self._price = val

# R-2.5
class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0): # R-2.7
        """
        Create a new credit card instance.

        :arg
        customer:   the name of the customer
        bank:       the name of the bank
        acnt:       the acount identifier(eg., '1234 1234 5555 5555')
        limit:      credit limit
        balance:    the default initial balance is zero.
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def charge(self, price):
        try:
            price = float(price)
        except ValueError:
            print("The input is not a number.\n")

        if price+self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("The input is not a number.\n")
        self._balance -= amount

# R-2.9 & 2.10
class Vector:
    """
    Represent a vector in a multidimensional space
    """
    # R-2.15
    def __init__(self, d):
        if type(d) is int:
            self._coords = [0]*d
        else:
            self._coords = d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    #2.11
    def __radd__(self, other):
        """Return sum of two vectors"""
        return self.__add__(other)

    # 2.9
    def __sub__(self, other):
        """Return subtraction of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    # 2.10
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result

    # 2.12 & 2.14
    def __mul__(self, other):
        if type(other) is int:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
            return result
        else:
            if len(self) != len(other):
                raise ValueError('dimensions must agree!')
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result

    # 2.13
    def __rmul__(self, other):
        return self.__mul__(other)



# P-2.33
###Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial.
import re
def f_prime(polynomial):
    """
    :arg polynomial like f(x) = 2*x^5 + 3*x^2 + x - 1 input as a list [-1,1,3,0,0,2] in assent order
    outputs: the first derivative of that polynomial
    """
    coeff = []
    for i in range(1, len(polynomial)):
        coeff.append(polynomial[i] * i)
    return coeff

# P-2.36
import random
class Bear:
    pass
class Fish:
    pass
# Bear = 'Bear'
# Fish = 'Fish'
class Ecosystem(object):
    def __init__(self, n_bear=2, n_fish=3, n=10):
        self.bear = n_bear
        self.fish = n_fish
        self.river = [None for _ in range(n)]
        self.initSet()

    def initSet(self):
        n_bear = self.bear
        n_fish = self.fish
        while n_bear:
            i = random.randrange(len(self.river))
            if self.river[i] is None:
                self.river[i] = Bear()
                n_bear -= 1

        while n_fish:
            i = random.randrange(len(self.river))
            if self.river[i] is None:
                self.river[i] = Fish()
                n_fish -= 1

        print(self.river)

    def randomProcess(self):
        pass

    def collide(self, i, j):
        obj1 = self.river[i]
        obj2 = self.river[j]
        if type(obj1) == type(obj2):
            c = random.randrange(len(self.river))
            if self.river[c] is None:
                self.river[c] = Fish() if isinstance(obj1, Fish) else Bear()
        else:
            if isinstance(obj1, Fish):
                self.river[i] = None
            else:
                self.river[j] = None






if __name__ == '__main__':
    v = Vector(5)
    v[1] = 4
    v[2] = 5
    u = Vector([1,2,3,4,5])
    x = u + v
    # print(x._coords)
    # print(f_prime([-1,1,3,0,0,2]))
    e = Ecosystem()
