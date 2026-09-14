class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] #(index, temp)
        out = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(s) != 0:
                while len(s) > 0 and s[-1][1] < t:
                    out[s[-1][0]] = i - s[-1][0]
                    s.pop()
            s.append((i, t))
        return out