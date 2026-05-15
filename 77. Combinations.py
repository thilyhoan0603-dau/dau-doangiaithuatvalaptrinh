class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path):
            # Goal: If the path has k elements, we found a combination
            if len(path) == k:
                res.append(list(path))
                return
            
            # Choice: Iterate from 'start' to 'n'
            # Optimization: only go up to n - (k - len(path)) + 2 
            # to ensure there are enough numbers left to pick
            for i in range(start, n + 1):
                path.append(i)
                # Recurse: Move to the next number
                backtrack(i + 1, path)
                # Backtrack: Remove the number to try the next choice
                path.pop()
                
        backtrack(1, [])
        return res