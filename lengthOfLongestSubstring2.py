class Solution:
    # @param {string} s
    # @return {integer}
    # My own thought: 左右夹挤法，加右边的减左边的； 用hashset维护
    # 更好的方法： 用hashmap记录上次出现的点；与最后起始点j 对比。
    # 更更好的方法：用array[char][256]维护这个hashmap
    # Scarlett chen
    # leetcode 3 Longest Substring Without Repeating Characters 
    # 5/23/2015
    def lengthOfLongestSubstring(self, s):
    	n = len(s)
    	if n<2:
    		return len(s)
    	start = 0
    	# like hashmap
    	usedChar = {}
    	maxlen = 0
    	for i in range(n):
    		if s[i] in usedChar:
    			start = max(start, usedChar[s[i]]+1)
    		usedChar[s[i]] = i
    		maxlen = max(maxlen, i - start+1)
    	return maxlen

        
