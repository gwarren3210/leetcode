from collections import defaultdict, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        hm = Counter(nums)
        if  k < (len(nums) / math.log2(len(nums))):
            h = [(v,k) for k,v in hm.items()]
            heapq.heapify_max(h)
            out = []
            for i in range(k):
                out.append(heapq.heappop_max(h)[1])
            return out
        else:
            l = sorted(list(hm.items()), key=lambda x:x[1], reverse=True)
            return [a for a,b in l[:k]]