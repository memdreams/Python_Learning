"""
<Data Structure and Algorithms in Python> Chapter 1

Date: 2018.03.11
Author: Jie
"""

# R-1.1
def is_multiple(n, m):
    return True if n % m == 0 else False

# R-1.2
def is_even(k):
    s = str(bin(k))
    return True if s[-1]=='0' else False

# R-1.3
def minmax(data):
    MIN = MAX = data[0]
    for i in data:
        if MIN > i:
            MIN = i
        if MAX < i:
            MAX = i
    return (MIN, MAX)

# R-1.4 & R-1.5
def sum_square(n):
    if n <= 1:
        return -1
    # squareList = [i*i for i in range(n)]
    return sum([i*i for i in range(n)])

# R-1.6 & R-1.7
def sum_odd_square(n):
    if n <= 1:
        return -1
    # squareList = [i*i for i in range(1, n, 2)]
    return sum([i*i for i in range(1, n, 2)])

# R-1.8
def equal_index(s):
    n = len(s)
    for i in range(1, n+1):
        k = -i
        j = n+k
        if s[k] == s[j]:
            print(k, s[k])

# R-1.9 range(50, 81, 10)
# R-1.10 range(8, -9, -2)
# R-1.11
l = [2**i for i in range(9)]

# R-1.12
from random import randrange
def choice(data):
    n = len(data)
    i = randrange(0, n)
    return data[i]



# Test
print(choice(l))




