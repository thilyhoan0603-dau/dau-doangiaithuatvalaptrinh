class Solution(object):
    def permute(self, nums):
        res = []
        
        def backtrack(current_perm):
            # Nếu hoán vị hiện tại đã đủ các số, lưu vào kết quả
            if len(current_perm) == len(nums):
                res.append(list(current_perm))
                return
            
            for num in nums:
                # Kiểm tra xem số này đã được dùng chưa
                if num not in current_perm:
                    # 1. Chọn số
                    current_perm.append(num)
                    
                    # 2. Đệ quy để chọn số tiếp theo
                    backtrack(current_perm)
                    
                    # 3. Quay lui: Bỏ số vừa chọn để thử số khác
                    current_perm.pop()
        
        backtrack([])
        return res
