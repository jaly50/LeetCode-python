class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    # Scarlett Chen
    # 6/3/2015
    def isScramble(self, s1, s2):
        m = len(s1)
        n= len(s2)
        if s1==s2:
            return True
        if m!=n: 
            return False
        if sorted(s1)!=sorted(s2):
            return False
        for i in range(1,m):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
        
