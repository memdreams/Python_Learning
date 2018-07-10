# 2018.06.26
# Try Multi-inheritance

import pprint
import cProfile

class A(object):
    def go(self):
        print("A")

class B(A):
    def go(self):
        super(B, self).go()
        print("B")

class C(A):
    def go(self):
        super(C, self).go()
        print("C")

class D(B, C):
    # pass
    def go(self):
        super(D, self).go()
        print("D")

# b = B()
# d = D()

# b.go()
# d.go()
# cProfile.run('d.go()')
# pprint.pprint(D.__mro__)

def solution1(N):
    # write your code in Python 3.6
    gap = 0
    maxGap = 0
    flag = 0
    while N>0:
        if N % 2 == 1:
            flag = 1

        if (N % 2 == 0 and flag == 1):
            gap += 1
            if (N/2) % 2 == 1:
                flag = 0
                maxGap = max(gap, maxGap)
                gap = 0
        N = N>>1

    return maxGap


def solution2(A):
    # write your code in Python 3.6
    N = len(A)
    S = set(A)
    if N != len(S):
        return 0
    total_N = sum(i for i in range(1, N+1))
    total_A = sum(A)
    return 1 if total_N==total_A else 0

def solution3(N, A):
    # write your code in Python 3.6
    r = [0 for ii in range(N)]
    for i in A:
        if i < N:
            r[i] += 1
        elif i == N+1:
            m = max(r)
            r = [m for j in range(N)]
    return r


def solution4(A):
    # write your code in Python 3.6
    pairs = counter0 = counter1 = 0
    east = 0
    west = 1

    for index, direction in enumerate(A):
        if counter0 > 0 and direction == west:
            counter1 += 1
        if index == len(A)-1:
            pairs += counter0 * counter1
            return pairs if pairs <= 1000000000 else -1
        if direction == east:
            pairs += counter0 * counter1
            counter0 += 1
            counter1 = 0




def fib(n):
    a, b = 0, 1
    while (a<n):
        print(a, end=' ')
        a, b = b, a+b
    print()



a = [0, 1, 0, 1, 1, 1, 0]
N = 5
# fib(2000)

def ask_ok(prompt, retries = 4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("Invalid user response")
        print(reminder)

def askfor(k, *args, **kwargs):
    print(k)
    print(args)
    for index, v in kwargs.items():
        print(index, v, end=',')
    print()

import json


with open('netperf', 'w') as f:
    # f.write(b'0123456789abcdef')
    # print(f.seek(5))
    # print(f.tell())
    # readdata = f.read(1)
    # print(f.tell())
    # print(f.seek(-3, 2))
    # print(f.read(1))
    x = [1, 2, 'a']
    json.dump(x, f)

with open('netperf', 'r') as f:
    x = json.load(f)
    s = f.read()
    print(s)



# for n in range(2,10):
#     for x in range(2, n):
#         if n%x == 0:
#             print(n, ':', x, "*", n//x)
#             break
#     else:
#         print(n, "is a prime.")

