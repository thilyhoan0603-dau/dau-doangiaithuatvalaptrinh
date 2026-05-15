class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # 1. Xử lý hàng đầu tiên (chỉ có thể đi từ trái sang)
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
            
        # 2. Xử lý cột đầu tiên (chỉ có thể đi từ trên xuống)
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            
        # 3. Xử lý các ô còn lại
        for i in range(1, m):
            for j in range(1, n):
                # Chọn đường đi có tổng nhỏ hơn giữa ô trên và ô trái
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[m-1][n-1]