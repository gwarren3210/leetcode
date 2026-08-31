class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * (n)

    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]
    
    def union(self, a, b):
        s1 = self.size[a]
        s2 = self.size[b]
        pA = self.find(a)
        pB = self.find(b)
        if pA == pB: return False
        if s2 > s1:
            self.par[pA] = pB
            self.size[pB] += self.size[pA]
        else:
            self.par[pB] = pA
            self.size[pA] += self.size[pB]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def md(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        edges = []
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                edges.append([md(points[i], points[j]), i, j])
        
        dsu = DSU(n)
        edges.sort()
        out = 0
        for dist, i, j in edges:
            if dsu.union(i,j):
                out += dist
        return out



