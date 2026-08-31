class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')':'(', ']':'[', '}':'{'}
        for l in s:
            if l in '({[': stack.append(l)
            elif not stack or stack[-1] != m[l]: return False
            else: stack.pop()
            
        return not stack