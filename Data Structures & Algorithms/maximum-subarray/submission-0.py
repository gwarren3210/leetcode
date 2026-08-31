class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = prev = nums[0]
        for n in nums[1:]:
            prev = max(n, prev+n)
            m = max(m, prev)
        return m