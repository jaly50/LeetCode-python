class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    # scarlett Chen
    # LeetCode sort Colors
    # in place one pass
    def sortColors(self, nums):
        i=j=k=0
        for num in nums:
            if num==2:
                nums[k]=2
                k+=1
            elif num==1:
                nums[k]=2
                k+=1
                nums[j]=1
                j+=1
            elif num==0:
                nums[k]=2
                k+=1
                nums[j]=1
                j+=1
                nums[i]=0
                i+=1
        
        
