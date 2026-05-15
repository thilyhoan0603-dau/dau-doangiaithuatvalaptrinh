# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        
        # Sentinel node to simplify head-related logic
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Move prev to the node right before the reversal starts
        for _ in range(left - 1):
            prev = prev.next
            
        # 2. curr is the first node to be reversed
        curr = prev.next
        
        # 3. Perform the reversal
        for _ in range(right - left):
            nxt = curr.next
            # Step-by-step pointer manipulation:
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            
        return dummy.next