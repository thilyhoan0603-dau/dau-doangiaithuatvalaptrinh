class Solution(object):
    def isMatch(self, s, p):
        s_ptr = 0
        p_ptr = 0
        last_s_match = 0
        star_idx = -1
        
        while s_ptr < len(s):
            # 1. Hai ký tự khớp nhau hoặc pattern là '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # 2. Gặp dấu '*', ghi nhớ vị trí và tạm thời coi như khớp 0 ký tự
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                last_s_match = s_ptr
                p_ptr += 1
            
            # 3. Không khớp nhưng trước đó có dấu '*', ta backtrack
            elif star_idx != -1:
                p_ptr = star_idx + 1 # Quay lại vị trí sau dấu '*'
                last_s_match += 1    # Cho '*' khớp thêm 1 ký tự trong s
                s_ptr = last_s_match
                
            # 4. Không khớp và không có dấu '*' nào để bấu víu
            else:
                return False
        
        # Kiểm tra xem các ký tự còn lại trong pattern có toàn là '*' không
        # Vì '*' có thể khớp với chuỗi rỗng
        return all(x == '*' for x in p[p_ptr:])
        