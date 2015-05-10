class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # make them only traverse once
        # try to save more space by using int[] as bits
        if board==None:
            return False
        rows = [0 for i in range(9)]
        cols = [0 for i in range(9)]
        box = [0 for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                term = 1<<(int)(board[i][j])
                inb =  (i/3)*3+j/3
                # those elements already exists in that area
                if (term & rows[i]) or (term & cols[j]) or (term & box[inb]):
                    return False
                else:
                    # If they don't exist
                    rows[i] = rows[i] | term
                    cols[j] = cols[j] |term
                    box[inb] = box[inb] |term
                    
        return True
        
