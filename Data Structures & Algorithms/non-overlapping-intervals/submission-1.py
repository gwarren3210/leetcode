class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        out = 0
        curEnd = intervals[0][1]
        print(intervals)
        for i in range(1, len(intervals)):
            print(i, curEnd)
            if intervals[i][0] < curEnd:
                out += 1
                curEnd = min(curEnd, intervals[i][1])
            else:
                curEnd = intervals[i][1]
        return out