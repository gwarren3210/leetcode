from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for a in asteroids:
            if a > 0: stack.append(a)
            elif stack and stack[-1] < 0:
                stack.append(a)
            else:
                while stack and stack[-1]>0 and -a > stack[-1]:
                    stack.pop()
                if stack:
                    if stack[-1] < 0:
                        stack.append(a)
                    if -stack[-1] == a:
                        stack.pop()
                else:
                    stack.append(a)
        return list(stack)
                