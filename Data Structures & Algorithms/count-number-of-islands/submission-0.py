class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        out = 0
        def dfs(x, y):
            if (x,y) in visited: return
            if x >= len(grid[0]) or x < 0 or y >= len(grid) or y < 0: return
            visited.add((x,y))
            if grid[y][x] == "0": return
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
                
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == "0": visited.add((i,j))
                if (i,j) in visited: continue
                dfs(i,j)
                out += 1
        return out