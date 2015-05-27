class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # Scarlett Chen
    # 5/27/2015 Wed 9:48 am
    # 遇到一样的，后面就不要理了。
    # 每次加一个元素；试图把这个元素放在每一个位置上
    def permuteUnique(self, nums):
        nums.sort()
        ans=[]
        ans.append([nums[0]])
        n = len(nums)
        for i in range(1, n):
            newans=[]
            for seq in ans:
                for j in range(i+1):
                    # a better and elegant way
                    # newll = seq[:j]+nums[i]+seq[j:]  
                    newll=[]
                    newll.extend(seq)
                    newll.insert(j, nums[i])
                    # print newll
                    newans.append(newll)
                    if j<i and seq[j]==nums[i]:
                        break
                    
            ans = newans
        return ans
        
