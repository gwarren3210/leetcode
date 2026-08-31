import pandas as pd
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        t = 0
        isT = False
        maxLeft = pd.Series(height).cummax().tolist()
        maxRight = pd.Series(height[::-1]).cummax().tolist()[::-1]
        print(maxRight)
        for i, h in enumerate(height):
            t += max(min(maxLeft[i], maxRight[i])-h,0)
            print(maxLeft[i], maxRight[i], h, t)
        return t

