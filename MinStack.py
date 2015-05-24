import sys
# Scarlett Chen
# 5/24/2015 Sun 6:16 PM
# LeetCode 155 Min Stack
# one stack and one min number, store realValue - min; 
class MinStack:
    def __init__(self):
        self.stack=[]
        self.mini = sys.maxint
    # @param x, an integer
    # @return an integer
    
    def push(self, x):
        self.stack.append(x-self.mini)
        if self.stack[-1]<0:
            self.mini= x
        return x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x <0:
            self.mini = self.mini - x
        
        

    # @return an integer
    def top(self):
        if self.stack[-1] <0:
            return self.mini
        else:
            return self.stack[-1]+self.mini
        
        

    # @return an integer
    def getMin(self):
        return self.mini
        
