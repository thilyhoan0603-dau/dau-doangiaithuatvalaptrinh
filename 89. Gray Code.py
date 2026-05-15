class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Start with the base case for n = 0 (or n = 1)
        res = [0]
        
        for i in range(n):
            # Calculate the value of the bit we are adding (2^i)
            bit_to_add = 1 << i
            
            # Mirror the current results and add the new bit
            # We iterate backwards through 'res' to create the reflection
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | bit_to_add)
                
        return res