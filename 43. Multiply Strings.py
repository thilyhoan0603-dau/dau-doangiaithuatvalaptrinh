class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Mảng chứa kết quả trung gian
        res = [0] * (len(num1) + len(num2))
        
        # Duyệt ngược từ cuối lên đầu của cả 2 số
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Nhân 2 chữ số (dùng int() cho từng ký tự là hợp lệ)
                mul = int(num1[i]) * int(num2[j])
                
                # Cộng vào vị trí tương ứng trong mảng res
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                res[p2] = total % 10    # Giữ lại hàng đơn vị
                res[p1] += total // 10   # Cộng dồn phần nhớ vào hàng chục
        
        # Chuyển mảng số thành chuỗi, loại bỏ số 0 ở đầu
        result_str = "".join(map(str, res))
        return result_str.lstrip("0")
