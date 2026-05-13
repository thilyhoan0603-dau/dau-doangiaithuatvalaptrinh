class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next

            prev.next = b
            a.next = b.next
            b.next = a

            prev = a

        return dummy.next
