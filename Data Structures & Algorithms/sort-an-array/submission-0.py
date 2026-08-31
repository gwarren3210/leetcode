class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        if len(nums) == 2: 
            return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]
        left = self.sortArray(nums[:len(nums)//2])
        right = self.sortArray(nums[len(nums)//2:])
        out = []
        l,r = 0,0
        if len(left) == 0: return right
        if len(right) == 0: return left
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                out.append(left[l])
                l += 1
            else:
                out.append(right[r])
                r+=1
        if l == len(left): out += right[r:]
        elif r == len(right): out += left[l:]
        return out