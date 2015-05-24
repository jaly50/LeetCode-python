class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    # LeetCode 97 Interleaving String
    # dp 两重循环 f[i][j] = f[i][j-1] 
    # make all by myself
    # scarlett chen
    # 5/24/2015 Sun 5:50 pm
    def isInterleave(self, s1, s2, s3):
        # 边界情况要记得先考虑
        if len(s3)!=len(s1)+len(s2):
            return False
        dp =[[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0]=True
        for i in range(1,len(s1)+1):
            dp[i][0] = True if s3[0:i]==s1[0:i] else False
        for j in range(1,len(s2)+1):
            dp[0][j]= True if s3[0:j]==s2[0:j] else False
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[len(s1)][len(s2)]
        
