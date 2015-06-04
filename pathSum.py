# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Jiali Chen
# 6/3/2015 Wed 8:27 PM
# Path Sum
class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -=root.val
        if (root.left==None and root.right==None):
            if sum==0:
                return True
        if self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum):
            return True
        return False
        
