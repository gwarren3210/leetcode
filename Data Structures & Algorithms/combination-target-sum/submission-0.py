class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()
        def dfs(i, l, curr):
            if curr == target:
                out.append(l.copy())
                return
            if i >= len(nums) or curr > target:
                return
            l.append(nums[i])
            dfs(i, l, curr + nums[i])
            l.pop()
            dfs(i+1, l, curr)
        dfs(0, [], 0)
        return out

