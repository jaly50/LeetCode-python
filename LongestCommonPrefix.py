#Scarlett Chen
#2015.03.03
#63ms
#check every character from left to right
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs or len(strs[0])==0:
            return ""
        length = len(strs[0])
        for i in range(length):
            ch=strs[0][i]
            for j in range(len(strs)):
                if len(strs[j])<=i or strs[j][i]!=ch:
                    return strs[0][:i]
        return strs[0]