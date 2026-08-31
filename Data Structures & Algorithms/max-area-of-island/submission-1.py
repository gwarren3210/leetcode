class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(x,y):
            if (x,y) in visited: return 0
            if x >= len(grid[0]) or x < 0 or y >= len(grid) or y<0: return 0
            visited.add((x,y))
            if grid[y][x] == 0: return 0
            return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y-1) + dfs(x,y+1)
        
        area = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                area = max(area, dfs(i,j))
            
        return area