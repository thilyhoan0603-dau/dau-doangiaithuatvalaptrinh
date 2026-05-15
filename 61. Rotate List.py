# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # 1. Tính độ dài n và tìm tail
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
            
        # 2. Biến thành vòng tròn
        curr.next = head
        
        # 3. Tìm vị trí cắt mới
        # Vị trí cắt là (n - k % n)
        k = k % n
        steps_to_new_tail = n - k
        
        new_tail = curr # Đang ở vị trí cuối cũ
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # 4. Thiết lập head mới và cắt vòng
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head