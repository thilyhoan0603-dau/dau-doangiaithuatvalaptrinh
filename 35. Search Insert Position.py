class Solution(object):
    def searchInsert(self, nums, target):
        # Thụt lề tất cả các dòng dưới đây vào 1 cấp (thường là 4 dấu cách)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
