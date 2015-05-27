class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # I hate recursive dfs....Too manyy parameters!!!!
    # a recursive way use permute itself with short lines
    # this method is amazing! I didn't thought about this.
    # Scarlett Chen
    # 5/26/2015 tue 10:14 pm
    # 46 Permutations
    # 反复循环元素也是一个iterative的好方法： https://leetcode.com/discuss/19510/my-ac-simple-iterative-java-solution
    def permute(self, nums):
        if len(nums)<=1:
            return [nums]
        perm=[]
        for idx,ele in enumerate(nums):
            for rest in self.permute(nums[:idx]+nums[idx+1:]):
                if rest:
                    perm.append([ele]+rest)
        return perm
