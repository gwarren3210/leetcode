from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(s):
            l = [0]*26
            for c in s:
                l[ord(c)-ord('a')] += 1
            out = ''
            for i in range(26):
                out += chr(ord('a')+i) +':'+str(l[i])
            return out
        hm = defaultdict(list)
        for s in strs:
            hm[counter(s)].append(s)
        return [v for v in hm.values()]