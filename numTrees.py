class Solution:
    # @param {integer} n
    # @return {integer}
    # scarlett chen
    # leetcode 96 Unique Binary Search Trees 
    # 5/24/2015
    # 重点是找到规律： f[i] = sum(f[j]* f[i-j-1]) (j in range(0,i))
    def numTrees(self, n):
        f=[0 for i in range(0,n+1)]
        f[0]=1
        f[1]=1
        for i in range(2, n+1):
            ans = 0
            for j in range(0,i):
                ans += f[j]*f[i-j-1]
            f[i]= ans
        return f[n]
        
