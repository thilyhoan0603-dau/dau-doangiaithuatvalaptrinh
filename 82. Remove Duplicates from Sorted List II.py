# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Sentinel node points to head
        sentinel = ListNode(0, head)
        
        # predecessor: the last node before the sublist of duplicates
        pred = sentinel
        
        while head:
            # If it's the beginning of a duplicate sublist
            if head.next and head.val == head.next.val:
                # Move until the end of the duplicate sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # Skip all duplicates
                pred.next = head.next
            else:
                # No duplicate, move predecessor forward
                pred = pred.next
                
            # Move head forward
            head = head.next
            
        return sentinel.next