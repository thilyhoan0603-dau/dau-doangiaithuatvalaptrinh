import math

class Solution(object):
    def getPermutation(self, n, k):
        # Tạo danh sách các số [1, 2, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Tính giai thừa (factorial) cho các bước nhảy
        # factorials[i] sẽ lưu i!
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
            
        # Điều chỉnh k về chỉ số 0
        k -= 1
        result = []
        
        # Xác định từng vị trí từ n xuống 1
        for i in range(n - 1, -1, -1):
            # i là số lượng các số còn lại phía sau vị trí hiện tại
            # index = k // (số lượng hoán vị của các số còn lại)
            idx = k // factorials[i]
            k %= factorials[i]
            
            # Thêm số tương ứng vào kết quả và xóa khỏi danh sách
            result.append(numbers[idx])
            numbers.pop(idx)
            
        return "".join(result)
