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
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort() # Bắt buộc phải sort để loại bỏ trùng lặp
        
        def backtrack(remain, comb, start):
            if remain == 0:
                res.append(list(comb))
                return
            
            for i in range(start, len(candidates)):
                # QUAN TRỌNG: Loại bỏ các số trùng lặp ở cùng một cấp độ
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Nếu số hiện tại lớn hơn số dư, các số sau cũng vậy (do đã sort)
                if candidates[i] > remain:
                    break
                
                comb.append(candidates[i])
                # i + 1 vì mỗi phần tử chỉ dùng 1 lần
                backtrack(remain - candidates[i], comb, i + 1)
                comb.pop()
        
        backtrack(target, [], 0)
        return res
>>>>>>> 93219ed (update file)
