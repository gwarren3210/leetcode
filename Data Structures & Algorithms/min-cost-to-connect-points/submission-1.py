class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i: [] for i in range(n)}
        def md(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        for i in range(n):
            for j in range(i+1, n):
                dist = md(points[i], points[j])
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        out = 0
        s = set()
        minH = [[0, 0]]
        while len(s)<n:
            cost, i = heapq.heappop(minH)
            if i in s: continue
            out += cost
            s.add(i)
            for nc, nei in adj[i]:
                if nei in s: continue
                heapq.heappush(minH, [nc, nei])
        return out