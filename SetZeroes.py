class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    # Scarlett Chen
    # 5/24/2015 Sun 7:33 pm
    #  73   Set Matrix Zeroes
    def setZeroes(self, matrix):
        #  把[0][0] leave to first row, since it will be calculate first
        # and the first col value will be record specially
        col0 = 1
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0]==0:
                col0 = 0
                break
        # 把col取出了以后，一定要注意范围！！！！  不能再把第一竖的值赋[0][0] 为0.否则会影响第一行的值的
        for i in range(n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in reversed(range(n)):
            for j in reversed(range(1,m)):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
            if col0==0:
                matrix[i][0]=0
  
        
