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
    
class Solution:
    # Total Hamming distance Calculation; ultilize the property: the distance in each bit is the multiple between ones and zeros.
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distance = 0

        for i in range(32): 
            ones = 0
            zero = 0
            for num in nums:
                if num & (1<<i):
                    ones+=1
                else:
                    zero+=1
            distance += ones * zero 
        
        return distance

    # 3. Given a string, find the length of the longest substring without repeating characters.
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        if len(s):
            noRepeat = s[0]
            r = 1
            for i in range(1, len(s)):
                if s[i] in noRepeat:
                    r = max(len(noRepeat), r)
                    noRepeat = noRepeat[(noRepeat.index(s[i])+1) : ] + s[i]
                else:
                    noRepeat += s[i]
            r = max(len(noRepeat), r)
        return r    
        
    
