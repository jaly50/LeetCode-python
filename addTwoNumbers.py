# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    # Scarlett Chen
    # 5/22/2015
    def addTwoNumbers(self, l1, l2):
        l3 = head = ListNode(0)
        carry =0
        while l1!=None or l2!=None:
            first = 0 if l1==None else l1.val
            second = 0 if l2==None else l2.val
            carry += first + second
            l3.next = ListNode(carry % 10)
            carry /= 10
            l3 = l3.next
            if l1!=None: 
                l1 = l1.next
            if l2!=None: 
                l2 = l2.next
        if carry !=0:
            l3.next = ListNode(carry)
        return head.next        
            
        
