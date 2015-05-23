# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 5/23/2015
# Scarlett Chen
# 83 Remove Duplicates from Sorted List
# One pass == too easy


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        first = head
        if head ==None or head.next==None:
            return head
        # at least two elements
        while head !=None and head.next!=None:
            right = head.next
            if head.val == right.val:
                head.next = right.next
            else:
                head = head.next
        return first
        
