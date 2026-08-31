class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = { i:set() for i in range(n)}
        for f, t, p in flights:
            adj[f].add((t, p))
        seen = { src: [(0, 0)] } # cost, steps

        minH = [[0, src, 0]] # cost to get to, airport, steps
        while minH:
            print(minH)
            c, a, s = heapq.heappop(minH)
            if a == dst: return c
            if a not in seen:
                seen[a] = []
            seen[a].append((c,s))
            for d, dc in adj[a]:
                if d in seen: print(seen[d])
                if d in seen and seen[d][-1][-1]<s+1: continue
                if s == k and d != dst: continue
                heapq.heappush(minH, [c+dc, d, s+1])
        return -1