"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end = sorted([i.end for i in intervals])
        start = sorted([i.start for i in intervals])

        res = cur = 0
        e = s = 0
        while e<len(end) and s<len(start):
            if start[s] < end[e]:
                cur += 1
                res = max(res, cur)
                s += 1
            else:
                cur -= 1
                e += 1
        return res