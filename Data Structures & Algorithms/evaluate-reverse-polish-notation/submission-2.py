from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = 0
        s = deque()
        def op(o, a, b):
            if o == '+':
                return a+b
            if o == '-':
                return a-b
            if o == '*':
                return a*b
            if o == '/':
                return int(float(a)/b)
        for t in tokens:
            if t in '+-*/':
                b,a = s.pop(), s.pop()
                s.append(op(t, a, b))
            else:
                s.append(int(t))
        return s.pop()
