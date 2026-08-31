class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = d.get(num -1, 0) + d.get(num+1, 0) + 1
                d[num-d.get(num-1, 0)] = d[num+d.get(num+1, 0)] = d[num]
        res = [v for v in d.values()]
        return max(res) if res else 0 