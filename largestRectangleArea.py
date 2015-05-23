class Solution:
    # @param {integer[]} height
    # @return {integer}
    #  LeetCode Largest Rectangle in Histogram
    # Scarlett Chen
    # 5/23/2015
    # 用栈维护递增序列
    def largestRectangleArea(self, height):
        stack =[]
        i=0
        n = len(height)
        if n<2:
            return height[0] if n else 0
        height.append(0)
        maxArea = 0
        for i in range(0, n+1):
            while stack!=[] and height[stack[-1]] > height[i]:
                edge = stack.pop()
                if stack==[]:
                    cur = i*height[edge]
                else:
                    cur =(i-stack[-1]-1)*height[edge]
                maxArea = max(maxArea, cur)
            stack.append(i)
        return maxArea
                
            
