class Solution(object):
    def countAndSay(self, n):
        # Trường hợp cơ bản
        if n == 1: 
            return "1"
        
        # Lấy kết quả của số trước đó (đệ quy)
        prev = self.countAndSay(n - 1)
        
        result = ""
        i = 0
        while i < len(prev):
            count = 1
            # Đếm các ký tự giống nhau liên tiếp
            while i + 1 < len(prev) and prev[i] == prev[i+1]:
                i += 1
                count += 1
            
            # Ghi vào kết quả: [số lượng] + [ký tự]
            result += str(count) + prev[i]
            i += 1
            
        return result
