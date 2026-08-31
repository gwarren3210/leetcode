from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        twos = []
        fresh = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 2: twos.append((x,y))
                if grid[y][x] == 1: fresh += 1
        if fresh == 0: return 0
        seen = set()
        
        print(twos)
        q = deque(twos)
        minutes = -1
        while q and fresh >0:
            print(q)
            for _ in range(len(q)):
                x,y = q.popleft()
                if min(x,y) < 0 or x >= len(grid[0]) or y >= len(grid): continue
                if grid[y][x] == 0 or (x,y) in seen: continue
                seen.add((x,y))
                if grid[y][x] == 1:
                    grid[y][x] = 2
                    fresh -= 1
                q.append((x+1, y))
                q.append((x-1, y))
                q.append((x, y+1))
                q.append((x, y-1))
            minutes += 1
        print(grid)
        return minutes if fresh == 0 else -1
