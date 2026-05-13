class Solution(object):
    def canJump(self, nums):
        # Biến lưu vị trí xa nhất có thể nhảy tới
        max_reach = 0
        
        # Duyệt qua từng chỉ số của mảng
        for i in range(len(nums)):
            # Nếu vị trí hiện tại i lớn hơn max_reach, 
            # nghĩa là không bao giờ nhảy tới được điểm này
            if i > max_reach:
                return False
            
            # Cập nhật lại max_reach dựa trên vị trí hiện tại i 
            # và khả năng nhảy tối đa tại đó nums[i]
            max_reach = max(max_reach, i + nums[i])
            
            # Tối ưu: Nếu max_reach đã vượt quá hoặc bằng đích đến, trả về True luôn
            if max_reach >= len(nums) - 1:
                return True
                
        return True