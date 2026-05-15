class Solution(object):
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            
            elif char in "+-":
                # Dấu chỉ được ở đầu hoặc ngay sau e/E
                if i > 0 and s[i-1] not in "eE":
                    return False
            
            elif char in "eE":
                # e/E chỉ được xuất hiện nếu đã có số trước đó và chưa có e/E nào khác
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False # Phải có số sau e, nên tạm reset để kiểm tra
            
            elif char == ".":
                # Dấu chấm không được xuất hiện sau e/E hoặc nếu đã có dấu chấm rồi
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            
            else:
                # Ký tự lạ (abc, ...)
                return False
        
        # Kết quả cuối cùng phụ thuộc vào việc đã thấy chữ số nào chưa
        return seen_digit