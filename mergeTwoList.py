# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    # Scarlett chen
    # 5/23/2015
    # LeetCode 21 Merge Two Sorted Lists 
    def mergeTwoLists(self, l1, l2):
        head =l3= ListNode(0)
        while l1 !=None or l2!=None:
            if l1==None:
                l3.next = l2
                break
            elif l2==None:
                l3.next = l1
                break
            first = l1.val
            second = l2.val
            if first <second:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        return head.next
        
