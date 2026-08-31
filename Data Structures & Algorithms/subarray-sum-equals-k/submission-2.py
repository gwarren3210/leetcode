import functools
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out, s = 0, 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        for n in nums:
            s += n
            dif = s - k
            out += prefixSum[dif]
            prefixSum[s] += 1
        return out
