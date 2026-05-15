class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(index, path):
            # Every step in the recursion is a valid subset
            res.append(list(path))
            
            for i in range(index, len(nums)):
                # Include the current element
                path.append(nums[i])
                # Move onto the next elements
                backtrack(i + 1, path)
                # Backtrack: Remove the element to try the "exclude" path
                path.pop()
        
        backtrack(0, [])
        return res