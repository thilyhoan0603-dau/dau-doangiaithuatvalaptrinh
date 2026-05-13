class Solution:
    def solveSudoku(self, board): 
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if self.is_valid(board, r, c, num):
                            board[r][c] = num
                            
                            if self.solve(board):
                                return True
                            
                            # Backtrack: if placing 'num' doesn't lead to a solution
                            board[r][c] = "."
                    
                    # If no number from 1-9 works in this cell
                    return False
        return True

    def is_valid(self, board, r, c, num):
        for i in range(9):
            # Check row
            if board[r][i] == num:
                return False
            # Check column
            if board[i][c] == num:
                return False
            # Check 3x3 box
            # (r // 3) * 3 gives the starting row of the box
            # (c // 3) * 3 gives the starting column of the box
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == num:
                return False
        return True
