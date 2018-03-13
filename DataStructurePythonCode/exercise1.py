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


# C-1.13
def reverse(data):
    n = len(data)
    reverse_data = []
    for i in range(1, n + 1):
        reverse_data.append(data[-i])
    return reverse_data

# C-1.14
def pair_odd_product(data):
    odd_num = set()
    for i in data:
        if i % 2 != 0:
            odd_num.add(i)
            if len(odd_num) >= 2:
                return True
    return False

# C-1.15
def is_distinct(data):
    distinctSeq = set()
    for i in data:
        distinctSeq.add(i)
    if len(distinctSeq) == len(data):
        return True
    else:
        return False

# C-1.16 & C-1.17 (not work properly)
def scale(data, factor):
    for i, val in enumerate(data):
        # val *= factor
        data[i] *= factor
    return data

# C-1.18
l1 = [i*(i+1) for i in range(10)]

# C-1.19
alphaBata = [chr(i) for i in range(97, 97+26)]

# C-1.20
from random import randint
def shuffle(data):
    output = []
    while len(data)>0:
        i = randint(0, len(data)-1)
        output.append(data[i])
        data.remove(data[i])
    return output

# C-1.21
def reverse_input():
    done = False
    output = []
    # line = input("Please input: ")
    while not done:
        try:
            line = input("Please input: ")
            output.append(line)
        except EOFError:
            output.reverse()
            done = True
    return output
    # while line:
    #     output.append(line)
    # return output.reverse()


# P-1.29
def permutation(s):
    if len(s) == 1:
        return [s]
    perm_list = []
    for i in set(s):
        s_stripe = s.replace(i, '')
        z = permutation(s_stripe)

        for t in z:
            perm_list.append(i+t)
    return perm_list

import itertools
perm = itertools.permutations('catdog')


# Test
print('\n')
print(reverse_input())

# import time
#
# start = time.time()
# permutation('catdogabreiu')  #---Time:  148.95268416404724
# end = time.time()
# print("---Time: ", end-start)
# start = time.time()
# itertools.permutations('catdogabreiu') # ---Time:  0.00012803077697753906
# end = time.time()
# print("---Time: ", end-start)




