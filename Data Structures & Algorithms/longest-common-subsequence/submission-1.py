class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0]*(n1+1) for _ in range(n2+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[j][i] = 1+dp[j-1][i-1]
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        return dp[-1][-1]