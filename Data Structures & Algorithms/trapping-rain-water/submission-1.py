import pandas as pd
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        t = 0
        maxL = height[l]
        maxR = height[r]
        while l<r:
            if maxL <= maxR:
                t += max(min(maxL, maxR)-height[l],0)
                l += 1
                maxL = max(maxL, height[l])
            else:
                t += max(min(maxL, maxR)-height[r],0)
                r -= 1
                maxR = max(maxR, height[r])
        return t


