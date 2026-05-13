<<<<<<< HEAD
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        for i in range(n):
            # Trong khi nums[i] là số dương, nhỏ hơn n 
            # và nó chưa nằm đúng vị trí của nó (nums[nums[i]-1])
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # Đổi chỗ để đưa nums[i] về đúng "nhà" của nó
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Duyệt lại để tìm số bị thiếu đầu tiên
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Nếu từ 1 đến n đều đủ, thì số thiếu là n + 1
        return n + 1
=======
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        for i in range(n):
            # Trong khi nums[i] là số dương, nhỏ hơn n 
            # và nó chưa nằm đúng vị trí của nó (nums[nums[i]-1])
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # Đổi chỗ để đưa nums[i] về đúng "nhà" của nó
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
<<<<<<< HEAD
        backtrack(target, [], 0)
        return res
>>>>>>> 93219ed (update file)
=======
        # Duyệt lại để tìm số bị thiếu đầu tiên
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Nếu từ 1 đến n đều đủ, thì số thiếu là n + 1
        return n + 1
>>>>>>> d9bacad (update 41. First Missing Positive.py)
