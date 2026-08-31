import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-n for n in stones]
        heapq.heapify(s)
        while len(s) > 1:
            x,y = heapq.heappop(s), heapq.heappop(s)
            res = x-y
            if res == 0: continue
            heapq.heappush(s, res)
        return 0 if len(s) == 0 else abs(s[0])
