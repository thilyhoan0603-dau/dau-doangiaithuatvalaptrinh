class Solution(object):
    def uniquePaths(self, m, n):
        # Chúng ta chỉ cần một mảng một chiều để lưu trữ giá trị của hàng trước đó
        row = [1] * n
        
        # Duyệt qua từng hàng (bắt đầu từ hàng thứ 2)
        for i in range(1, m):
            # Duyệt qua từng cột (bắt đầu từ cột thứ 2)
            for j in range(1, n):
                # Giá trị mới = giá trị ô bên trái + giá trị ô phía trên (chính là row[j] cũ)
                row[j] = row[j] + row[j-1]
                
        return row[n-1]
