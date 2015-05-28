class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    # Scarlett Chen
    # 5/28/2015 Thu 12:36 pm
    # 79Word Search
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i,j,word,0):
                    return True
        return False
    def dfs(self,board, x,y, word, idx):
        # 注意判断循环的base和 终止条件！
        if idx>=len(word):
            return True
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]) or board[x][y]!=word[idx]:
            return False
        board[x][y]='`'
        ans = self.dfs(board, x-1, y, word, idx+1) \
        or self.dfs(board, x, y+1, word, idx+1) \
        or self.dfs(board, x+1, y, word, idx+1) \
        or self.dfs(board, x, y-1, word, idx+1)
        board[x][y]=word[idx]
        return ans
