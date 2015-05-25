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
    # LeetCode  99  Recover Binary Search Tree 
    # 5/24/2015 Sun 10:38 pm
    # o(1) space,特别的记得后继的方法 http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
    # 普通方法就是 recursive or iterative 用stack
    def recoverTree(self, root):
        prev = first = second = None
        cur = root
        while cur!=None:
            if cur.left ==None:
                if prev !=None and prev.val > cur.val:
                    if first==None:
                        first = prev
                        second = cur
                    else:
                        second = cur
                prev = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right!=cur and pre.right!=None:
                    pre = pre.right
                if pre.right==None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if prev !=None and prev.val > cur.val:
                        if first==None:
                            first = prev
                            second = cur
                        else:
                            second = cur
                    prev = cur
                    cur = cur.right
        if first!=None and second!=None:
            temp = first.val
            first.val = second.val
            second.val = temp
        
                    
        
