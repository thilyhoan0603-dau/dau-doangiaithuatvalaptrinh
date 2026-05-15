class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # 1. Sort the array to handle duplicates
        nums.sort()
        
        def backtrack(index, path):
            # Add the current subset to our results
            res.append(list(path))
            
            for i in range(index, len(nums)):
                # 2. Skip duplicates: 
                # If the current element is the same as the one before it
                # AND it's not the first element we're considering at this level.
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res