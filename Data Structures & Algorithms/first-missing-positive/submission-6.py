class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n <= 0:
                nums[i] = len(nums)+1

        for i, n in enumerate(nums):
            j = abs(n)
            if j-1<len(nums):
                nums[j-1] = -abs(nums[j-1])
        print(nums)
        for i, n in enumerate(nums):
            if n >= 0:
                return i+1
        return len(nums)+1