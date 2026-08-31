class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            r,l = i,i
            while l>=0 and r<len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1
            
            r,l = i+1,i
            while l>=0 and r<len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1
        return res