# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    # Scarlett Chen
    # 06/14/2015 Sun 4:59 pm
    # Morris. No recursive o1(space) without stack
    # Flatten Binary Tree to Linked List 
    def flatten(self, root):
        if not root:
            return
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        
