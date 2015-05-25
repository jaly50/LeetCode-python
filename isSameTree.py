# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    # 超级简单
    # Scarlett Chen
    # 100 LeetCode isSameTree
    # 5/24/2015 Sun 10:42PM
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        return p.val ==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
