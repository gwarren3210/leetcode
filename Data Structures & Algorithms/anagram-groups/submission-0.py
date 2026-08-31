from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            c = ''.join(sorted(s))
            if c in m:
                m[c].append(s)
            else:
                m[c] = [s]
        return m.values()