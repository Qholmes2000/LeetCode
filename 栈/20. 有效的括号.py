class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        if len(s) % 2 != 0:
            return False
        

        # 构建括号映射表
        mapping = {')' : '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack