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
       
    # 201. Bitwise AND of Numbers Range
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        while m != n:
            shift += 1
            m = m >> 1
            n = n >> 1
        
        return m << shift
    
    
    ## 385. Mini Parser
    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger:
    #    def __init__(self, value=None):
    #        """
    #        If value is not specified, initializes an empty list.
    #        Otherwise initializes a single integer equal to value.
    #        """
    #
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def add(self, elem):
    #        """
    #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
    #        :rtype void
    #        """
    #
    #    def setInteger(self, value):
    #        """
    #        Set this NestedInteger to hold a single integer equal to value.
    #        :rtype void
    #        """
    #
    #    def getInteger(self):
    #        """
    #        @return the single integer that this NestedInteger holds, if it holds a single integer
    #        Return None if this NestedInteger holds a nested list
    #        :rtype int
    #        """
    #
    #    def getList(self):
    #        """
    #        @return the nested list that this NestedInteger holds, if it holds a nested list
    #        Return None if this NestedInteger holds a single integer
    #        :rtype List[NestedInteger]
    #        """
    
    # actually, in python, this function can just be implemented by eval(s)
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        
        
        nestedS = NestedInteger()
        stackList = []
        digits, neg = None, 1
        
        for c in s:
            if c == '-':
                neg = -1
            elif c.isdigit():
                digits = (digits or '') + c
            if c == '[':
                stackList.append(NestedInteger())
            else:
                if digits is not None:
                    stackList[-1].add(NestedInteger(int(digits) * neg))
                    digits, neg = None, 1
                if c == ']':
                    top = stackList.pop()
                    if stackList:
                        stackList[-1].add(top)
                    else:
                        return top
    
