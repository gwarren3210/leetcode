from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        maxH = [(v,k) for k,v in c.items()]
        heapq.heapify_max(maxH)
        out = []
        for _ in range(k):
            out.append(heapq.heappop_max(maxH))
        return [k for _,k in out]