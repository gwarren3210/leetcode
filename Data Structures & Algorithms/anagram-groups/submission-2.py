from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # Counter --> list
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return [val for val in d.values()]