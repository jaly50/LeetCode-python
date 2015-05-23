# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Scarlett Chen
# 5/23/2015
# LeetCode 82 Remove Duplicates from Sorted List II 
# refer  a little bit: pre and next relations, amazing

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        first = ListNode(0)
        first.next = head
        pre = first
        duplicate = False
        while head!=None:
            while head!=None and head.next!=None and head.val == head.next.val:
                head = head.next
            if pre.next == head:
                pre = head
            # delete duplicate --the only element
            else:
                pre.next = head.next
            head = head.next
                
        
        return first.next
        
