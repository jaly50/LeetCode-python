# Scarlett Chen
# 6/3/2015 Wed 8:15 pm
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        sum = [[2147483647 for i in range(m)] for j in range(n)]
        sum[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i>0:
                    sum[i][j] = min(sum[i-1][j]+grid[i][j], sum[i][j])
                if j>0:
                    sum[i][j] = min(sum[i][j-1] + grid[i][j], sum[i][j])
        return sum[n-1][m-1]
                
        
