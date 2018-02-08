# Leetcode Easy Task Collection


# 643. Maximum Average Subarray I
class Solution:
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

