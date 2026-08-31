class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(a,b):
            return math.sqrt(a**2 + b**2)
        h = []
        for a,b in points:
            heapq.heappush(h, (dist(a,b), (a,b)))
        return [x[1] for x in heapq.nsmallest(k,h)]