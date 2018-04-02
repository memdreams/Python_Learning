"""
<Data Structure and Algorithms in Python> Chapter 4

Date: 2018.04.01
Author: Jie
"""

# chapter 4 Recursion
def factorial(n):
    """ Return the factorial of n; n is an non-negative integer
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
# the runnning time of factorial(n) & factorial1(n) is similar, but recursion method has the maximum recursion depth limit
def factorial1(n):
    """ Return the factorial of n; n is an non-negative integer
    """
    if n == 0:
        return 1
    pre_result = 1
    for i in range(1, n+1):
        pre_result *= i
    return pre_result

# Draw an English Ruler
def draw_ruler(inches, majorLen):
    """need to call draw_line() and draw_interval()"""
    draw_line(majorLen, '0')
    for i in range(1, inches+1):
        draw_interval(majorLen - 1)
        draw_line(majorLen, str(i))


def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' '+tick_label
    print(line)

def draw_interval(central_length):
    if central_length > 0:
        draw_interval(central_length-1)
        draw_line(central_length)
        draw_interval(central_length-1)

# Binary Search
def binSearch(l, target, low, high):
    """ l is a sorted list. """
    n = len(l)
    if low > high:
        return False
    else:
        middle = (low+high)//2
        if l[middle] == target:
            return True
        elif l[middle] > target:
            return binSearch(l, target, low, middle-1)
        else:
            return binSearch(l, target, middle+1, high)

import os
def disk_usage(path):
    """ Return the bytes used by a file/folder and any descendents """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total


# R-4.1


import time
if __name__ == '__main__':
    # start1 = time.time()
    # factorial(100)
    # end1 = time.time()
    # elapse1 = end1 - start1
    #
    # start2 = time.time()
    # factorial1(100)
    # end2 = time.time()
    # elapse2 = end2 - start2

    # print(binSearch([1,2,3,4,5,6,8,9], 8, 0, 7))
    disk_usage('/Users/Dreams/UOttawa/Study/DataStructure/pythonCode')