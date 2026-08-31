class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        s = nums[0]
        out = len(nums)+1
        for l in range(len(nums)):
            while s < target and r < len(nums)-1:
                r += 1
                s += nums[r]
            if s<target: break
            out = min(out, r-l+1)
            s -= nums[l]
        return out if out != len(nums)+1 else 0