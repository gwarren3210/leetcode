from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        m = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '({[':
                stack.append(c)
            elif len(stack) == 0 or m[c] != stack.pop():
                return False
        return len(stack) == 0