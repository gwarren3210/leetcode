from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        zeros = []
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 0:
                    zeros.append((x,y, 0))
        seen = set()
        print(seen)
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        q = deque(zeros)
        while q:
            x, y, s = q.popleft()
            print(x,y,s)
            if x >= len(grid[0]) or x < 0 or y >= len(grid) or y<0:
                continue
            if grid[y][x] == -1 or (x,y) in seen: continue
            seen.add((x,y))
            grid[y][x] = s
            s += 1
            for dx, dy in directions:
                q.append((x+dx, y+dy, s))