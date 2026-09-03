class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        longest = 0
        numset = set(nums)
        for n in numset:
            left  = hm.get(n-1, 0)
            right = hm.get(n+1, 0)
            length = left + 1 + right
            hm[n] = length
            hm[n-left] = length
            hm[n+right] = length
            longest = max(longest, length)
        return longest
