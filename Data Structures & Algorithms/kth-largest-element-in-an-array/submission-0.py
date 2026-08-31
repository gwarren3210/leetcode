class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        h = [-n for n in h]
        return heapq.nlargest(k, h)[-1]