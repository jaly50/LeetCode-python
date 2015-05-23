class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    # 5/22/2015
    # Scarlett Chen
    # Wildcard Matching
    def isMatch(self, s, p):
        i,j=0,0
        star = -1
        while (i<len(s)):
            if j<len(p) and (s[i]==p[j] or p[j]=='?'):
                i+=1
                j+=1
            elif j<len(p) and p[j]=='*':
                match = i
                star = j
                j+=1
            # match means new index after matching *; * might match 0,1,2 elements
            elif star!=-1:
                match+=1
                i= match
                j= star+1
            # when there is no star and not match
            else:
                return False
        while j<len(p) and p[j]=='*':
            j+=1
        return j==len(p)
            
