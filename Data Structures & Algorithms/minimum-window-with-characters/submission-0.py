from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        sc = defaultdict(int)
        substring = out = ""
        r = 0
        missing = set(tc.keys())
        for l in range(len(s)):
            while len(missing)>0 and r<len(s):
                sc[s[r]]+=1
                substring += s[r]
                if s[r] in missing and sc[s[r]] >= tc[s[r]]:
                    missing.remove(s[r])
                r += 1
            if len(missing)>0: break
            if len(substring) < len(out) or out == "":
                out = substring
            sc[s[l]] -= 1
            substring = substring[1:]
            if sc[s[l]] < tc[s[l]]:
                missing.add(s[l])
        return out