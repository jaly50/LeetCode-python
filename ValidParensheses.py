class Solution:
    # @param {string} s
    # @return {boolean}
    # Scarlett Chen
    # Valid Parentheses 
    # 6/6/2015 Sat 10:59 PM
    def isValid(self, s):
        stack = []
        for c in s:
            if c in ['(','{','[']:
                stack.append(ord(c))
            elif stack and ord(c) - stack[-1] <=2:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
        
