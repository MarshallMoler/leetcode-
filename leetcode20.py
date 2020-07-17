'''有效的括号'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        map = {"}":"{","]":"[",")":"("}
        for char in s:
            if char in map:
                top_elem = stack.pop() if stack else "#"
                if map[char] != top_elem:
                    return False
            else:
                stack.append(char)
        return not stack
