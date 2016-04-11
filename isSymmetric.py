# Recursive way
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def same(self, leftside, rightside):
        if not leftside and not rightside:
            return True
        if not leftside or not rightside:
            return False
        return leftside.val==rightside.val and self.same(leftside.left, rightside.right) and self.same(leftside.right, rightside.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.same(root.left, root.right)
