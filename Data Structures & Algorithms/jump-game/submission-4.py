class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums) -1
        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= g:
                g = i
        return g == 0