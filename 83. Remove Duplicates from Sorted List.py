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
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Found a duplicate! Skip the next node
                current.next = current.next.next
            else:
                # No duplicate, move to the next unique node
                current = current.next
                
        return head