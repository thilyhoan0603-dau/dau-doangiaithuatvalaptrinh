class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(remain, comb, start):
            # Trường hợp tìm được kết quả
            if remain == 0:
                res.append(list(comb))
                return
            # Trường hợp tổng đã vượt quá target
            elif remain < 0:
                return
            
            # Duyệt qua các số trong candidates
            for i in range(start, len(candidates)):
                # Thử chọn số candidates[i]
                comb.append(candidates[i])
                
                # Gọi đệ quy: 
                # Vẫn giữ nguyên 'i' vì một số có thể dùng nhiều lần
                backtrack(remain - candidates[i], comb, i)
                
                # Quay lui: Bỏ số vừa chọn để thử số tiếp theo
                comb.pop()
        
        backtrack(target, [], 0)
        return res
