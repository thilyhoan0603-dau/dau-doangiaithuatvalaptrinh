class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Mảng dp lưu số cách đi đến từng cột trong hàng hiện tại
        dp = [0] * n
        
        # Trạng thái ban đầu tại ô (0,0)
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                # Nếu gặp vật cản, số cách đến ô này bằng 0
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                # Nếu không phải vật cản và không phải cột đầu tiên
                elif j > 0:
                    # Số cách mới = Cách từ ô trên (dp[j] cũ) + Cách từ ô trái (dp[j-1])
                    dp[j] += dp[j-1]
                    
        return dp[n-1]