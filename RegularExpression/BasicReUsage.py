"""
2018.07.09 Jie
 Practice Basic Regular Expression Operation.
"""

import re

def is_allowed_special_symbol(s):
    p = re.compile(r'\W')
    # p = re.compile(r'[^a-zA-Z0-9]')
    s = p.search(s)
    return not bool(s)

s1 = 'ASDGw245ew3.'
s2 = '-=-]['

print(is_allowed_special_symbol(s1))
print(is_allowed_special_symbol(s2))

