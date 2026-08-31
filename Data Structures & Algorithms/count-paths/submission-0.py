class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[float('inf')]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                temp = 0
                if i > 0: temp += dp[i-1][j]
                if j > 0: temp += dp[i][j-1]
                dp[i][j] = temp
        return dp[-1][-1]