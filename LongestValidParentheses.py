class Solution:
    # @param s, a string
    # @return an integer
    #奇妙的解法！在栈中保留不能配队的index...他们之间的距离就是他们中间有多少个配队的
    #第一个位置放），可以有效排除一开始没人可以减的情况，也以空栈溢出的情况－－棒棒棒
    def longestValidParentheses(self, s):
        s=")"+s
        stack, ans=[],0
        for index in xrange(len(s)):
            ele=s[index]
            if ele==')' and stack and stack[-1][1]=='(':
                stack.pop()
                ans=max(ans,index-stack[-1][0])
            else:
                stack.append((index, ele))
        return ans
                
                    
        
