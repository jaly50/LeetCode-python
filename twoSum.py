# 只要求index1 < index2,所以不需要排序！
# 要返回的是index，所以不能排序。不然会乱了index
# Scarlett Chen
# 6/3/2015 Wed 6:34 PM
# Two Sum
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        map={}
        for idx, ele in enumerate(nums):
            if (target - ele) in map:
                return [map[target-ele], idx+1]
            map[ele]=idx+1
        return None
        
