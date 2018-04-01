"""
<Data Structure and Algorithms in Python> Chapter 3

Date: 2018.04.01
Author: Jie
"""
import numpy as np
import matplotlib.pyplot as plt

# R-3.1
# Graph the functions 8n, 4nlog n, 2n2, n3, and 2**n using a logarithmic scale for the x - and y - axes;
# that is, if the function value f (n) is y, plot this as a point with x - coordinate at logn and y-coordinate at logy.
def graph_f(n):
    t = np.arange(1.0, n, 10)

    plt.plot(t, 8*t, 'r--', t, 4*t*np.log(t), 'bs', t, 2*t**2, 'g^', t, t**3, linewidth=1.0)
    plt.yscale('log')
    plt.xscale('log')
    plt.title('log')
    plt.grid(True)
    plt.show()

# R-3.2 n0 >= 2
# The number of operations executed by algorithms A and B is 8nlog n and2n^2, respectively.
# Determine n0 such that A is better than B for n ≥ n0.

# R-3.3 n0 >= 20

# R-3.4 ...


if __name__ == '__main__':
    graph_f(100)

