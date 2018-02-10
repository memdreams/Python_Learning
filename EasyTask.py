# Leetcode Easy Task Collection

class Solution:
    
    # 643. Maximum Average Subarray I
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if k>n:
            return False
        if n < 1 or n > 30000:
            return False
        
        sumSubNums = sum(nums[0:k])
        subNums = sumSubNums
        for i in range(k, n):
            subNums = subNums + nums[i] - num[i-k]
            sumSubNums = max(sumSubNums, subNums)
        
        return sumSubNums/k


    # 14. Longest Common Prefix
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        listLen = len(strs)
        if listLen == 0:
            return ""
        pre = strs[0]
        for i, string in enumerate(strs):
            width = max(len(pre), len(string))
            while width > 0:
                if pre[:width] == string[:width]:
                    pre = pre[:width]
                    break
                else:
                    width -= 1
            if width == 0:
                return ""
        return pre

    # Find if c satisfy a*a + b*b = c
    def judgeSquareSum(c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        a = 0
        b = int(math.sqrt(c))
        # squarelist = [x*x for x in range(0, iternum+1)]
        while a <= b:
            if a * a + b * b == c:
                print(a, b)
                return True
            elif a * a + b * b < c:
                a += 1
            else:
                b -= 1

    return False

    # 461. Hamming Distance
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = x^y
        distance = 0
        while c > 0:
            c = c&(c-1)
            distance += 1
        
        return distance

