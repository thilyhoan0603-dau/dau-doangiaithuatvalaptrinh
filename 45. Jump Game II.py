class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Chúng ta không cần duyệt đến phần tử cuối cùng 
        # vì khi đến sát nút, ta đã tính được cú nhảy cuối rồi.
        for i in range(n - 1):
            # Cập nhật điểm xa nhất có thể chạm tới
            farthest = max(farthest, i + nums[i])
            
            # Nếu đã đi hết phạm vi của cú nhảy hiện tại
            if i == current_end:
                jumps += 1            # Phải nhảy thêm một bước
                current_end = farthest # Ranh giới mới là điểm xa nhất vừa tìm được
                
                # Nếu ranh giới mới đã phủ đến cuối mảng, dừng luôn
                if current_end >= n - 1:
                    break
                    
        return jumps
