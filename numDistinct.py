class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    # Scarlett Chen
    # 6/9/2015 Tue 1:06 AM
    # Distinct Subsequences 
    def numDistinct(self, s, t):
        n = len(s)
        m = len(t)
        f = [[0 for i in range(m+1)] for j in range(n+1)]
        // first initianization
        f[0][0] =1
        for i in range(1,n+1):
            for j in range(m+1):
                if j==0:
                # when no match, the initialization is 1
                    f[i][j] = 1
                else:
                # both of them have to be one
                    f[i][j] = f[i-1][j] + f[i-1][j-1]*(s[i-1]==t[j-1])
        return f[n][m]
        
