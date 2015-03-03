#Longest Substring Without Repeating Characters
#2015.03.03
#by Scarlett Chen
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        hashtable=[-1] * 128
        left=0
        max=0
        for right in range(0,len(s)):
            if hashtable[ord(s[right])] >=left:  
                left=hashtable[ord(s[right])]+1
            hashtable[ord(s[right])]=right
            max=right-left+1 if right-left+1>max else max
        return max
        