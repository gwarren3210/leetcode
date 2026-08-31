class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += str(len(s))+':'+s
        return out
    def decode(self, s: str) -> List[str]:
        out = []
        i = j = 0
        while i<len(s):
            i = s.find(':', j)
            if i == -1: break
            n = int(s[j:i])
            out.append(s[i+1:i+n+1])
            j = i+n+1
        return out