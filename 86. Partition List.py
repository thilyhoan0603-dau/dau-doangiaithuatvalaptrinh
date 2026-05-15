# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Create dummy nodes for the two partitions
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to the current last nodes of the two partitions
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
            
        # Crucial: terminate the "after" list to avoid cycles
        after.next = None
        
        # Connect the two lists
        before.next = after_head.next
        
        return before_head.next