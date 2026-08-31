from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = defaultdict(list) # index --> list
        for key, value in Counter(nums).items():
            buckets[value].append(key)
        max_freq = max(buckets.keys())
        out = []
        for i in range(max_freq, 0, -1):
            out.extend(buckets[i])
        return out[:k]