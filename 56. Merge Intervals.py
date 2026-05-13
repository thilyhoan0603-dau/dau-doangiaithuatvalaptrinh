class Solution(object):
    def merge(self, intervals):
        # 1. Sắp xếp các khoảng theo điểm bắt đầu
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # Nếu danh sách merged trống hoặc không có sự chồng lấn
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Có sự chồng lấn, ta cập nhật điểm kết thúc của khoảng cuối cùng
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged