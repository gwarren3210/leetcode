class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(intervals)):
            print(out)
            if newInterval[0] > intervals[i][1]:
                out.append(intervals[i])
                continue
            if newInterval[1] < intervals[i][0]:
                out.append(newInterval)
                return out+ intervals[i:]
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
        print(out)
        out.append(newInterval)
        return out