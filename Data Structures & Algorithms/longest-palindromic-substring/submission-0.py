class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ''
        m = 0
        for i in range(len(s)):
            # odd
            for j in range(1+len(s)//2):
                if i+j >=len(s) or i-j<0: break
                if s[i+j] != s[i-j]: break
                if 2*j+1 > m:
                    print("entered")
                    out = s[i-j:i+j+1]
                    m = 2*j+1
            #even
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>m:
                    m = r-l+1
                    out = s[l:r+1]
                l -= 1
                r += 1
        return out