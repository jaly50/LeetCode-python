class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # 简单题
    # inplace solution
    # scarlett Chen
    # 26    Remove Duplicates from Sorted Array
    # 5/25/2015 mon 4:00 pm
    def removeDuplicates(self, nums):
        old = fresh = 0
        if not nums:
            return 0
        prev = None
        n = len(nums)
        while old < n:
            while prev!=None and old<n and nums[prev] ==nums[old]:
                old +=1
            if old >=n:
                break
            nums[fresh] = nums[old]
            prev = fresh
            fresh+=1
            old+=1
               
        return fresh
        
