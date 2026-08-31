from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2): return False
        
        @cache
        def dfs(i, j):
            if i >= len(s1) and j >= len(s2): return True
            res = False
            if i < len(s1) and s3[i+j] == s1[i]:
                res = res or dfs(i+1, j)
            if j < len(s2) and s3[i+j] == s2[j]:
                res = res or dfs(i, j+1)
            return res
        return dfs(0,0)