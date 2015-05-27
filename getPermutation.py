class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    # 60Permutation Sequence
    # Scarlett Chen
    # 5/27/2015 Wed 12:32
    # k－1 除以 (n-1)! 商即第一位的值  －－k = k%(i)! 反复执行
    def getPermutation(self, n, k):
        array=[str(i) for i in range(1,n+1)]
        k = k-1
        ans=""
        for i in range(n-1, -1,-1):
            idx, k = divmod(k, math.factorial(i))
            ans+=array.pop(idx)
        return ans
            
        
        
