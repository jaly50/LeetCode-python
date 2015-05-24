class Solution:
    # @param {integer} n
    # @return {integer}
    # 只要考虑5出现的次数。
    # 25里包含两个5; 第一个5的时候在n/5里算过了，这里只要再算一次就好了。
    # scarlett chen
    # leetcode 172 Factorial Trailing Zeroes
    # 5/23/2015 Sat 10:17 pm
    def trailingZeroes(self, n):
        base = 5
        ans =0
        while n>=base:
            ans += n/base
            base *=5
        return ans
