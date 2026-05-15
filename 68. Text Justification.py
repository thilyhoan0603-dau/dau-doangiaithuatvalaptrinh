class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            # Kiểm tra xem thêm từ 'w' vào dòng hiện tại có vượt quá maxWidth không
            # (num_of_letters + độ dài từ mới + số khoảng trống tối thiểu giữa các từ)
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Giai đoạn phân phối khoảng trắng cho dòng hiện tại
                for i in range(maxWidth - num_of_letters):
                    # Chia đều khoảng trống vào các từ trong cur (trừ từ cuối cùng)
                    # Nếu chỉ có 1 từ, len(cur)-1 = 0, sẽ rơi vào trường hợp append cuối
                    cur[i % (len(cur) - 1 or 1)] += ' '
                
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            
            cur.append(w)
            num_of_letters += len(w)
            
        # Xử lý dòng cuối cùng: Căn lề trái, các từ cách nhau 1 dấu cách
        last_line = " ".join(cur)
        remaining_spaces = maxWidth - len(last_line)
        res.append(last_line + ' ' * remaining_spaces)
        
        return res