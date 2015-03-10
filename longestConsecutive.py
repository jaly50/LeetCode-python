class Solution:
    # @param num, a list of integer
    # @return an integer
    # 用一个set维护〜找到最长子序列！
    def longestConsecutive(self, num):
        nums=set(num)
        maxlen=0
        while nums:
            m=n=nums.pop()
            len=1
            while m-1 in nums:
                nums.remove(m-1)
                m-=1
                len+=1
            while n+1 in nums:
                nums.remove(n+1)
                n+=1
                len+=1
            maxlen=max(maxlen,len)
        return maxlen
        
