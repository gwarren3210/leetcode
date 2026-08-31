class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        indegree = [[0]*COLS for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in [(0,1), (1,0), (-1, 0), (0,-1)]:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS: continue
                    if matrix[r][c] < matrix[nr][nc]:
                        indegree[r][c] += 1
        
        q = []
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    q.append((r,c))
        
        out = 0
        while q and out < ROWS*COLS:
            print(q)
            for _ in range(len(q)):
                r,c = q.pop(0)
                for dr, dc in [(0,1), (1,0), (-1, 0), (0,-1)]:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS: continue
                    if matrix[r][c] > matrix[nr][nc]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr,nc))
            out += 1
        return out