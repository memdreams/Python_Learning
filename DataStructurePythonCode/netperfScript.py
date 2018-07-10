"""
# Description:
#    This program runs netperf benchmark utility automatically for setting times and analyze the result.
#    Input: n, running times
#    Output: ave_through, the average throughput of n times
# History:
# 2018.4.14     Meng, Jie     First releases
"""

import os
import sys
# import subprocess

path = "./"
tool = "netperf"

# status = os.system('sh '+tool)
n = int(sys.argv[1]) if len(sys.argv)>1 else 10  # running n times

total_through = 0
for time in range(n):
    result = os.popen('sh ' + tool).readlines()  # or other execute command
    i = -1
    while result[i] is '\n' or None:  # or the other kind of space line
        i -= 1
    data = result[i].split()
    total_through += float(data[-1])
    # print(total_through)
ave_through = total_through/n
print(n, "times average throughput:", ave_through, "10^6bits/sec")


