class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        # 1. Check if first row/col have zeroes
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
        
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                
        # 2. Use first row/col as markers for the rest of the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 3. Set zeroes based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 4. Handle the first row and col markers themselves
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0