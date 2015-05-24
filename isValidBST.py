# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    # 要注意 Node和int的区别，参数要写对。
    # 用了min和max value,用了除了把握儿子的大小； 同时还确保左儿子的右儿子要小于root
    # Scarlett Chen
    # leetcode 98 Validate Binary Search Tree
    # 5/24/2015
    def isValidBST(self, root):
        return self.control(root, -sys.maxint, sys.maxint)
      
    def control(self, root, minvalue, maxvalue):
        if root ==None:
            return True
        if root.val <=minvalue or root.val >= maxvalue:
            return False
        return self.control(root.left, minvalue, root.val) and self.control(root.right, root.val, maxvalue)
                
        
