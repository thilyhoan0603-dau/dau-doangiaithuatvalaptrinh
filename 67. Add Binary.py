class Solution:
    def addBinary(self, a, b):
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        
        while i >= 0 or j >= 0 or carry:
            # Lấy giá trị tại i/j nếu còn, nếu hết thì mặc định là 0
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0
            
            total = val_a + val_b + carry
            res = str(total % 2) + res # Cộng chuỗi trực tiếp để không cần reverse
            carry = total // 2
            
            i -= 1
            j -= 1
            
        return res