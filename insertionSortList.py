# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    # scarlett chen
    # 5/23/2015 sat 9:08 pm
    # Leetcode Insertion Sort List 
 def insertionSortList(self, head):
        pre =dummy = ListNode(-1)
        cur = head
        # 有一组数据已排好序，按这个方法会超时。所以在这里判断一下。
        while cur!=None:
            # optimization for sorted list
            if pre.val >=cur.val:
                pre = dummy
            while pre.next !=None and pre.next.val < cur.val:
                pre = pre.next
            temp = cur.next
            cur.next = pre.next
            pre.next =cur
            cur = temp
        return dummy.next
            
