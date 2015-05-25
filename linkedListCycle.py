# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#  简单题，自己写，一次过
# Scarlett Chen
# 5/25/ 2015 Mon 10:54 am
# LeetCode 141   Linked List Cycle  36.3%   Medium
# 双指针： 一快一慢

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        first = second = head
        if head==None or head.next ==None:
            return False
        while (second !=None):
            first = first.next
            second = second.next
            if second!=None:
                second = second.next
            if first == second:
                return True
        return False
        
