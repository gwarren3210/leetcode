class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            n = max(nums[i] + dp[0], dp[1])
            dp = [dp[1], n]
        return max(dp)