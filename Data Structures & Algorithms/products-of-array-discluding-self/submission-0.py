class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = nums.copy()
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i]
        post = nums
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i]*nums[i+1]
        res = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[0] = post[1]
            elif i == len(nums)-1:
                res[i] = pre[i-1]
            else:
                res[i] = pre[i-1]*post[i+1]
        return res