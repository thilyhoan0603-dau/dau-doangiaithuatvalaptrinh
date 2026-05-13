class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Bước 1: Chuyển vị (Transpose)
        for i in range(n):
            # Chỉ chạy j từ i để không bị đổi chỗ 2 lần (trở về như cũ)
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Bước 2: Đảo ngược từng hàng (Reverse)
        for i in range(n):
            matrix[i].reverse()
