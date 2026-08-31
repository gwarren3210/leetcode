class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        sub = []
        def dfs(i):
            if i >= len(nums):
                out.append(sub.copy())
                return
            dfs(i+1)
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()

        
        dfs(0)
        return out