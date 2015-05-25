# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# scarlett Chen
# 5/25/2015 Mon 11:23 Am
# 142 Linked List Cycle II 
# 双指针，龟兔赛跑

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        first = second =head
        if head ==None or head.next ==None:
            return None
        while second !=None:
            first = first.next
            second = second.next
            if second!=None:
                second = second.next
            if first == second:
                first = head
                # 注意head 也有可能是cycle的起点，所以要先判断。不能先往前走。!!!!
                while first!=second:
                    first = first.next
                    second = second.next
                return first
        return None

                    
            
        
