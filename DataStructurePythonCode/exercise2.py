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

