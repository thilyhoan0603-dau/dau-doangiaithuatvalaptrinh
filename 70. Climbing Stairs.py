class Solution(object):
    def climbStairs(self, n):
        # Các trường hợp cơ bản
        if n <= 2:
            return n
        
        # first tương ứng f(n-2), second tương ứng f(n-1)
        first, second = 1, 2
        
        # Tính toán từ bậc thứ 3 đến n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second