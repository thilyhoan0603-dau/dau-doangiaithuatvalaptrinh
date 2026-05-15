class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(r, c, index):
            # Base Case: Found the whole word
            if index == len(word):
                return True
            
            # Boundary and character match check
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # Mark the current cell as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore neighbors: Up, Down, Left, Right
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            # Backtrack: Restore the cell for other paths
            board[r][c] = temp
            
            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
                    
        return False