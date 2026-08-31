from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            c = ''.join(sorted(s))
            d[c].append(s)
        return d.values()