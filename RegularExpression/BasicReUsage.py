"""
2018.07.09 Jie
 Practice Basic Regular Expression Operation.
"""

import re

# 1. check if a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
def is_allowed_special_symbol(s):
    p = re.compile(r'\W')  # the same as: p = re.compile(r'[^a-zA-Z0-9]')
    s = p.search(s)
    return not bool(s)

# 2. matches a string that has an 'a' followed by 0 or more 'b''s.
# 3. an 'a' followed by one or more b's
# 4. an 'a' followed by zero or one 'b'
# 5. an 'a' followed by 3 'b's
# 6. an 'a' followed by 2 to 3 'b's
# 7. find sequences of lowercase letters joined with a underscore
# 8. find sequences of one upper case letter followed by lower case letters.
# 9. a string that has an 'a' followed by anything, ending in 'b'.
# 10. matches a word at the beginning of a string.
# 11. matches a word at end of string, with optional punctuation.
# 12. matches a word containing 'z'.
# 13. a word containing 'z', not start or end of the word.
def is_matched(s):
    p = r'ab*?'  # 2
    p = r'ab+?'  # 3
    p = r'ab?'  # 4
    p = r'ab{3}?'  # 5
    p = r'ab{2,3}?'  # 6
    p = r'^[a-z]+_[a-z]+$'  # 7
    p = r'^[A-Z][a-z]+$'  # 8
    p = r'a.*?b$'  # 9  Q: difference between r'a.*?b$' and r'a.*b$'
    p = r'^\w+'  # 10
    p = r'\w+\S*$'  # 11
    p = r'\w*z\w*?'  # 12 '\w*z.\w*'  why?
    p = r'\Bz\B'  # 13
    m = re.search(p, s)
    return bool(m)








s1 = '[ab[ ASDGw245ew3.'
s2 = '-=-]['
s3 = 'Abbbbabbbbbbbb'

print(is_matched(s1))
print(is_matched(s3))

