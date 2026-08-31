class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = nums[0]
        curMin = curMax = 1
        for num in nums:
            temp = curMin
            curMin = min(num*curMin, num*curMax, num)
            curMax = max(num*temp, num*curMax, num)
            out = max(out, curMax, curMin)
            #print(num, out, curMax, curMin)
        return out