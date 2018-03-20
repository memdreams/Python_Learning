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
    while not done:
        try:
            line = input("Please input: ")
            output.append(line)
        except EOFError:
            output.reverse()
            done = True
    return output

# C-1.22
def arrayDotProduct(a, b):
    if len(a) != len(b):
        return -1
    c = []
    for i in range(len(a)):
        product = a[i]*b[i]
        c.append(product)
    return c

# C-1.23
def catchIndexError(l, i):
    try:
        l[i]
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")

# C-1.24
def countVowels(s):
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    countV = 0
    for i in s:
        if i in vowelsList:
            countV += 1
    return countV

# C-1.25
def keepChars(s):
    A = 65
    Z = 90
    a = 97
    z = 122
    for i in s:
        if (ord(i) > z or ord(i) < A or Z < ord(i) < a) and i != ' ':
            s = s.replace(i, '')
    return s

# C-1.26
def isFormula(a, b, c):
    if (a+b == c) or (a == b-c) or (a * b == c) or (a / b == c):
        print('%d + %d = %d\n', a, b, c)
        return True
    else:
        return False

# C-1.27
def factors(n):  # generator that computes factors
    k = 1
    bignums = []
    while k*k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            bignums.append(n // k)
        k += 1
    if k*k == n:  # special case if n is perfect square
        yield k
    bignums.reverse()
    for i in bignums:
        yield i

# C-1.27
def norm(v, p=2):
    return pow(sum([pow(i, p) for i in v]), 1/p)


# P-1.29 Solution1
def permutation(s):  # time consuming
    if len(s) == 1:
        return [s]
    perm_list = []
    for i in set(s):
        s_stripe = s.replace(i, '')
        z = permutation(s_stripe)

        for t in z:
            perm_list.append(i+t)
    return perm_list
# P-1.29 Solution2 don't understand well
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

import itertools
perm = itertools.permutations('catdog')

# P-1.30
def countMulti2(n):
    count = 0
    while n>1:
        n /= 2
        count += 1
    return count

# P-1.31
def makeChange(charged, given):
    canadianDollars = {'dime':5, 'cent':10, 'quarter':25,
                       '1$':1, '2$':2,
                       '5$':5, '10$':10, '20$':20, '50$':50}
    changes = given - charged
    # waiting to do... just a if-else, don't want to list them all


# P-1.32 & 33 待做

# P-1.34 略

# P-1.35
import random
def birthParadox(n):
    testBirthdays = []
    for i in range(n):
        testBirthdays.append(str(random.randrange(1,31))+str(random.randrange(1,12)))
    singleBirthdays = set(testBirthdays)
    return len(testBirthdays)-len(singleBirthdays) # same birthdays number

# P-1.36
def countwords(l):
    words = l.split()
    wordscount = {}
    for word in words:
        wordscount[word] = wordscount.get(word, 0) + 1
    return wordscount


# Test
if __name__ == '__main__':
    print('\n')
    print(countwords('he is my husband not your husband hello my darling you are mine you and I he and she you'))

import time

# start = time.time()
# c = permutations((range(0,3)))
# for i in c:
#     next(c)
# # permutations('catdogabreiu') #---Time:  148.95268416404724
# end = time.time()
# print("---Time: ", end-start)
# start = time.time()
# itertools.permutations('catdogabreiu') # ---Time:  0.00012803077697753906
# end = time.time()
# print("---Time: ", end-start)




