# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Scarlett Chen
# Fri 10:21 AM 6/5/2015 
#Construct Binary Tree from Preorder and Inorder Traversal 
# A solution easy to understand
class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        # to reduce meomery usage, we pop the first element
        root = TreeNode(preorder.pop(0))
        j = inorder.index(root.val)
        if j==-1:
            return None
        root.left = self.buildTree(preorder , inorder[0:j])
        # After we find the left part,  the left part of preorder has already been empty
        root.right = self.buildTree(preorder, inorder[j+1:])
        return root
            
    
        
