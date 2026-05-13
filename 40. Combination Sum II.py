class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort() # Bắt buộc phải sort để loại bỏ trùng lặp
        
        def backtrack(remain, comb, start):
            if remain == 0:
                res.append(list(comb))
                return
            
            for i in range(start, len(candidates)):
                # QUAN TRỌNG: Loại bỏ các số trùng lặp ở cùng một cấp độ
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Nếu số hiện tại lớn hơn số dư, các số sau cũng vậy (do đã sort)
                if candidates[i] > remain:
                    break
                
                comb.append(candidates[i])
                # i + 1 vì mỗi phần tử chỉ dùng 1 lần
                backtrack(remain - candidates[i], comb, i + 1)
                comb.pop()
        
        backtrack(target, [], 0)
        return res
