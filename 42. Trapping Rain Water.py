class Solution(object):
    def trap(self, height):
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left < right:
            # Nếu cột bên trái thấp hơn bên phải, ta xử lý bên trái
            if height[left] < height[right]:
                # Cập nhật tường trái cao nhất từng thấy
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Nước đọng = tường cao nhất - chiều cao hiện tại
                    water += left_max - height[left]
                left += 1
            else:
                # Ngược lại, xử lý bên phải
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water
