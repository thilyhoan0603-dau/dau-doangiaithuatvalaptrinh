class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            node = prev
            for i in range(k):
                node = node.next
                if not node:
                    return dummy.next

            tail = prev.next
            curr = tail.next

            for i in range(k-1):
                tail.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = tail.next

            prev = tail
