# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    # Scarlett Chen
    # Leetcode 101 Symmetric Tree
    # date : 5/24/2015 Sun 5:02 pm
    # iterative way: two pointer, que
    def isSymmetric(self, root):
        queLeft = deque()
        queRight = deque()
        if root ==None:
            return True
        queLeft.append(root.left)
        queRight.append(root.right)
        # 判断deque是否为空的方法
        while queLeft and queRight:
            left = queLeft.popleft()
            right = queRight.popleft()
            if left==None and right ==None:
                continue
            if left==None or right ==None:
                return False
            if left.val != right.val:
                return False
            queLeft.append(left.left)
            queLeft.append(left.right)
            queRight.append(right.right)
            queRight.append(right.left)
        return True
        
        
        
        
