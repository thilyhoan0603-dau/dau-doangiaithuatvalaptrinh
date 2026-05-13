class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: find first decreasing element
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find next bigger element
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse right side
        nums[i+1:] = reversed(nums[i+1:])
