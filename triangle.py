class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    # Scarlett Chen
    # 6/9/2015 Tue 1:07 pm
    # Triangle
    def minimumTotal(self, triangle):
        n  = len(triangle)
        if n<1:
            return 0
        result =(1<<31) -1
        ans = [0 for i in range(n)]
        # precedence of addition and subtraction is higher than bitwise shift
        for i in range(n):
            for j in range(i,-1,-1):
                if i==0:
                    ans[j] = triangle[i][j]
                elif j==i and j>0:
                    ans[j] =ans[j-1]+triangle[i][j]
                elif j==0:
                    ans[j] = ans[j]+triangle[i][j]
                else:
                    ans[j] = min(ans[j],ans[j-1])+triangle[i][j]
                    
                if i==n-1:
                    result = min(result, ans[j])
        return result
                
        
        
