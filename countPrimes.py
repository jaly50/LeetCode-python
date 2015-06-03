# Scarlett Chen
# 6/3/2015 Wed 6:52 PM
# 要注意只要找<n的质量数量
# 拿空间换时间〜 这样子说是只需要（o nlog n )的时间
# Count primes
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        b = [True for i in range(n)]
        sq = int(math.sqrt(n))
        for i in range(2,sq+1):
            if not b[i]:
                continue
            for j in range(i*i, n,i):
                b[j] = False
        count =0
        for i in range(2, n):
            if b[i]:
                count+=1
        return count
            
        
