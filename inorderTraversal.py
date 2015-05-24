# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    # scarlett Chen
    # 5/24/2015
    # LeetCode Binary Tree Inorder Traversal 
    # inorder traversal using iterative method: a stack
    # remember to return intergers
    def inorderTraversal(self, root):
        order = []
        if root==None:
            return order
        stack = []
        pre = None
        while root!=None or stack!=[]:
            if root!=None:
                stack.append(root)
                root = root.left
            else:
               pop = stack.pop()
               order.append(pop.val)
               root = pop.right
        return order
               
        
        
