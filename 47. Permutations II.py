class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # Bước 1: Sắp xếp để dễ nhận diện số trùng
        used = [False] * len(nums)
        
        def backtrack(current_perm):
            # Nếu đã chọn đủ số, lưu vào kết quả
            if len(current_perm) == len(nums):
                res.append(list(current_perm))
                return
            
            for i in range(len(nums)):
                # Nếu vị trí này đã dùng rồi, bỏ qua
                if used[i]:
                    continue
                
                # QUAN TRỌNG: Loại bỏ trùng lặp
                # Nếu nums[i] giống nums[i-1] và nums[i-1] CHƯA được dùng
                # nghĩa là chúng ta đang thử lại cùng một giá trị ở cùng một vị trí
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Tiến hành chọn số
                used[i] = True
                current_perm.append(nums[i])
                
                backtrack(current_perm)
                
                # Quay lui (Backtrack)
                current_perm.pop()
                used[i] = False
        
        backtrack([])
        return res
