# Leetcode Medium Problems Solusion

# Find Repeated DNA sequences, only A, G, T, C in sequences
def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if len(s) <= 10:
        return []
    d = {}
    r = []
    for i in range(len(s)):
        substr = s[i:i + 10]
        d[substr] = d.get(substr, 0) + 1
    for key, value in d.items():
        if value > 1:
            r.append(key)
    return r
    
    
