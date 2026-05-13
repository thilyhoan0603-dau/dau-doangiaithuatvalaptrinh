class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # nếu là ngoặc đóng
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:  # ngoặc mở
                stack.append(char)

        return not stack
