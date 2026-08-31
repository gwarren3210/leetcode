class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n

        pre = 1
        for i in range(n):
            out[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(n-1, -1, -1):
            out[i] *= post
            post *= nums[i]

        return out