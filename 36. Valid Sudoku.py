class Solution(object):
    def isValidSudoku(self, board):
        # Tất cả các dòng dưới đây phải thụt lề vào so với "def"
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                # 1. Kiểm tra xem số này đã xuất hiện chưa
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False
                
                # 2. Quan trọng: Nếu chưa có, phải thêm nó vào set để kiểm tra cho các ô sau
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        return True
