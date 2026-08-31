class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > 0 and len(set(nums)) != len(nums)