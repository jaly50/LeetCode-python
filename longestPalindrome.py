# 05/20/2015
# 记录 以当前点为终点的最长回文子串 maxlen维护同时更新的最长串
# leetcode 5 Longest Palindromic Substring
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        maxlen = 0
        maxindex =0
        for i in range(len(s)):
            if isPalindrome(s, i-maxlen, i):
                maxlen+=1
                maxindex = i
            elif  i-maxlen-1>=0 and isPalindrome(s, i-maxlen-1, i):
                maxlen+=2
                maxindex =i
        return s[maxindex-maxlen+1: maxindex+1]
    
def isPalindrome(string, start, end):
    while (start <end):
        if string[start] != string[end]:
            return False
        start+=1
        end-=1
    return True
        
