class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Cập nhật tổng gần target nhất
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Di chuyển con trỏ
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current  # đúng target

        return closest
