# Pre-traverse the tree
# List as parameter is a reference. It didn't make deep copy, it is itself.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
import re
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        ans = str(root.val)
        return ans + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        
    def dezi(self, array):
        node = array.pop()
        if node =='None':
            return None
        root = TreeNode(int(node))
        root.left = self.dezi(array)
        root.right = self.dezi(array)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        nodes.reverse()
        return self.dezi(nodes)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
