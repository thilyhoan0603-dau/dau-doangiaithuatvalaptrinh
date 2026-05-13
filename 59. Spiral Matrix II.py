class Solution(object):
    def generateMatrix(self, n):
        # Khởi tạo ma trận n x n với các giá trị 0
        matrix = [[0] * n for _ in range(n)]
        
        # Khởi tạo các biên
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1 # Số bắt đầu điền
        
        while num <= n * n:
            # 1. Đi từ Trái sang Phải
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1 # Thu hẹp biên trên
            
            # 2. Đi từ Trên xuống Dưới
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1 # Thu hẹp biên phải
            
            # 3. Đi từ Phải sang Trái
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1 # Thu hẹp biên dưới
            
            # 4. Đi từ Dưới lên Trên
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1 # Thu hẹp biên trái
            
        return matrix
