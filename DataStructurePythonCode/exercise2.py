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

myfunc()  # only be decorated once
myfunc()

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

# myfunc = deco(myfunc) # is the same as @deco, only one of them can exist

myfunc1()
myfunc1()


# Test a loop in linked list
class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    @classmethod  # the decorator use as a Factory
    def count(cls, a):
        return cls(a)

def isCycled(head):
    slowP = fastP = head
    n = 0
    while (slowP and fastP and fastP.next):
        slowP = slowP.next
        fastP = fastP.next.next
        n += 1
        if slowP == fastP:
            print("The loop is found! {} times search.\n".format(n))
            return True

    print('There is no loop in the linked list!\n')
    return False

def creatNode():
    listNodes = []
    for i in range(10):
        node = ListNode(i)
        listNodes.append(node)

    for i, node in enumerate(listNodes):
        node.next = listNodes[(i+1)%10]
    return listNodes

# Test Case
listNodes = creatNode()
isCycled(listNodes[0])


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

    @property
    def price(self):
        return self._price


if __name__ == '__main__':
    a = Flower()
    b = Flower('iry', 3, 10)
    a.name = 'lily'
    print(b.petal)

