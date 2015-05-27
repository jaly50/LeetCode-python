class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    # Scarlett Chen
    # 5/27/2015 Wed 1:04 am
    # 31Next Permutation
    # done by myself, lean some sytax from others
    # 从右往左，找到第一个非递增数；与右边比它大的最小数交换，右边排序
    def nextPermutation(self, nums):
        n= len(nums)
        if n<=1:
            return
        i = n-1
        while i>0 and nums[i-1] >= nums[i]:
            i-=1
        if i==0:
            nums.reverse()
        else:
            x = n-1
            while nums[i-1] >= nums[x]: 
                x-=1
            nums[i-1],nums[x]=nums[x],nums[i-1]
            nums[i:]=sorted(nums[i:])
            
        
