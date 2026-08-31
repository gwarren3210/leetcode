from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for o in operations:
            #print(o,": ",stack, sep="")
            if o == "+":
                b,a = stack.pop(), stack.pop()
                stack.append(a)
                stack.append(b)
                stack.append(a+b)
            elif o == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(2*a)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)