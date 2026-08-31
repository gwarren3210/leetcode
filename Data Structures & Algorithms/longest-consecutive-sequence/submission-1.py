class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        length = 0
        for n in s:
            if n-1 in s:
                continue
            length = 1
            while n+length in s:
                length += 1
            longest = max(longest, length)
        return max(longest, length)