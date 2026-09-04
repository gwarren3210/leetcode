from collections import deque
class MinStack:

    def __init__(self):
        self.s = deque() # (val, min)

    def push(self, val: int) -> None:
        m = val
        if len(self.s) > 0:
            m = min(m, self.s[-1][1])
        self.s.append((val, m))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
        
