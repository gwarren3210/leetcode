class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        s  = [] # pair index, height
        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                index, height = s.pop()
                start = index
                m = max(m, (i-index)*height)
            s.append((start, h))
        for i,h in s:
            m = max(m, (len(heights)-i)*h)
        return m