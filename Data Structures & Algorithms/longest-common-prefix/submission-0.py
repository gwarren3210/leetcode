class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        m = min([len(s) for s in strs])
        for i in range(m):
            l = strs[0][i]
            for w in strs[1:]:
                if l != w[i]:
                    return out
            out += l
        return out