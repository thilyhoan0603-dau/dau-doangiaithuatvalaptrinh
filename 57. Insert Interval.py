class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        
        # Giai đoạn 1: Thêm các khoảng nằm hoàn toàn bên trái newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # Giai đoạn 2: Hợp nhất tất cả các khoảng chồng lấn với newInterval
        # Điều kiện chồng lấn: start của khoảng hiện tại <= end của newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Thêm khoảng mới đã được hợp nhất vào kết quả
        result.append(newInterval)
        
        # Giai đoạn 3: Thêm các khoảng còn lại nằm bên phải
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result