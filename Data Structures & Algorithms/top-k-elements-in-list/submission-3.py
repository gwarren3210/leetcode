from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(sorted(Counter(nums).items(), key=lambda x:x[0], reverse=True))
        return [x[0] for x in sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)][:k]