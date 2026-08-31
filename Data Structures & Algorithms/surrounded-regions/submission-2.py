class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ts = []
        ROWS = len(board)
        COLS = len(board[0])
        for c in range(COLS):
            if board[0][c] == "O": ts.append((0,c))
            if board[ROWS-1][c] == "O": ts.append((ROWS-1,c))
        for r in range(1,ROWS-1):
            if board[r][0] == "O": ts.append((r,0))
            if board[r][COLS-1] == "O": ts.append((r,COLS-1))
        print(ts)
        seen = set()
        def dfs(r,c):
            if min(r,c)<0 or r>= ROWS or c>= COLS or (r,c) in seen:
                return
            if board[r][c] == "X": return
            print(r,c)
            seen.add((r,c))
            board[r][c] = "T"
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        for r,c in ts:
            dfs(r,c)
        
        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c] == "T":
                    board[r][c] = "O"