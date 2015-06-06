class Solution:
    def __init__(self):
        self.ans =0
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        if n==1:
            return 1
        if n<=3:
            return 0
        self.ans=0
        all = (1<<n) -1;
        self.dfs(all,0,0,0)
        return self.ans
    
    def dfs(self, all,row, l, r):
        if row ==all:
            self.ans = self.ans+1
        else:
        # all possible position in horizontal would be 1
            pos = all & ~(row|l|r)
            while (pos>0):
            # to get the right most 1
                p = pos & (~pos+1)
                pos -=p
                # l and r is the diagnal left and right, if p is 1, in next row, p-1 could not be 1
                self.dfs(all, row|p, (l|p)<<1, (r|p)>>1)

                
            
