<<<<<<< HEAD
class Solution(object):
    def simplifyPath(self, path):
        # Bước 1: Tách chuỗi theo dấu '/'
        # split('/') sẽ tạo ra danh sách các tên thư mục, '.' và '..'
        components = path.split('/')
        stack = []
        
        for part in components:
            # Nếu gặp '..', quay lại thư mục cha (xóa phần tử cuối stack)
            if part == "..":
                if stack:
                    stack.pop()
            # Bỏ qua các trường hợp không cần thiết: 
            # chuỗi rỗng (do //), dấu chấm đơn '.'
            elif part == "." or part == "":
                continue
            # Các trường hợp còn lại là tên thư mục hợp lệ
            else:
                stack.append(part)
        
        # Bước 2: Nối lại thành đường dẫn chuẩn
        # Luôn bắt đầu bằng '/' và các thư mục cách nhau bởi '/'
        return "/" + "/".join(stack)
=======
class Solution(object):
    def simplifyPath(self, path):
        # Bước 1: Tách chuỗi theo dấu '/'
        # split('/') sẽ tạo ra danh sách các tên thư mục, '.' và '..'
        components = path.split('/')
        stack = []
        
        for part in components:
            # Nếu gặp '..', quay lại thư mục cha (xóa phần tử cuối stack)
            if part == "..":
                if stack:
                    stack.pop()
            # Bỏ qua các trường hợp không cần thiết: 
            # chuỗi rỗng (do //), dấu chấm đơn '.'
            elif part == "." or part == "":
                continue
            # Các trường hợp còn lại là tên thư mục hợp lệ
            else:
                stack.append(part)
        
        # Bước 2: Nối lại thành đường dẫn chuẩn
        # Luôn bắt đầu bằng '/' và các thư mục cách nhau bởi '/'
        return "/" + "/".join(stack)
>>>>>>> 09dacbd ( update file)
