class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # k is the write pointer. 
        # The first two elements are always allowed.
        k = 2
        
        # Start scanning from the third element
        for i in range(2, len(nums)):
            # If the current element is not the same as the element
            # two positions before the current write pointer...
            if nums[i] != nums[k - 2]:
                # ...then it's a valid element to keep.
                nums[k] = nums[i]
                k += 1
                
        return k