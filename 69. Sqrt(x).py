class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 0, x
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Để tránh tràn số trong một số ngôn ngữ như C++, 
            # người ta thường dùng mid <= x / mid thay vì mid * mid <= x
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans