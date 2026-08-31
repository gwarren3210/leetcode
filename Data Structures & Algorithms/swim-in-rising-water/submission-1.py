class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        s = set() # row, column
        n = len(grid)
        minH = [[0,0,0]] # elevation, row, column
        s.add((0,0))
        currE = grid[0][0]
        while minH:
            #print(minH)
            e, r, c = heapq.heappop(minH)
            dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
            currE = max(e, currE)
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if nr == n-1 and nc == n-1:
                    return max(currE, grid[nr][nc])
                if nr<0 or nr>=n or nc<0 or nc>=n or (nr,nc) in s:
                    continue
                heapq.heappush(minH, [max(e, grid[nr][nc]), nr, nc])
                s.add((nr, nc))
        
