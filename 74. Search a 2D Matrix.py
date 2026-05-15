class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map the 1D 'mid' back to 2D coordinates
            row = mid // n
            col = mid % n
            
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False