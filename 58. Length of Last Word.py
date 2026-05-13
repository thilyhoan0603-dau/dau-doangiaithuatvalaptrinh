class Solution(object):
    def lengthOfLastWord(self, s):
        # Cắt chuỗi thành danh sách các từ
        words = s.split()
        if not words:
            return 0
        # Trả về độ dài của phần tử cuối cùng trong danh sách
        return len(words[-1])
