class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] *(len(nums))
        dp[0] = True
        for i in range(len(nums)):
            #print(i, dp)
            if not dp[i] or nums[i] == 0: continue
            for j in range(nums[i]+1):
                if i+j >= len(nums): break
                #print(i,j, i+j)
                dp[i+j] = True

        return dp[-1]