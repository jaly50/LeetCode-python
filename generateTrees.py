# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# dp的代码简单漂亮。加上左儿子和右儿子所有的可能；遍历。
# Scarlett Chen
# 5/24/2015 Sun 4:28 pm
# LeetCode 95 Unique Binary Search Trees II 
class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        f = [[] for i in range(0, n+1)]
        f[0].append(None)
        for i in range(1, n+1):
            for j in range(0, i):
                for left in f[j]:
                    for right in f[i-j-1]:
                        node = TreeNode(j+1)
                        node.left = left
                        node.right = self.clone(right,j+1)
                        f[i].append(node)
        return f[n]
    
    def clone(self, root, offset):
        if root ==None:
            return root
        # 注意要赋新的变量。否则原来的node值会被变化掉。
        Node = TreeNode(root.val+offset)
        Node.left = self.clone(root.left,offset)
        Node.right = self.clone(root.right, offset)
        return Node
                        
        
