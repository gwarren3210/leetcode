from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = list(accumulate([1]+nums, operator.mul))
        #print(pre)
        post = list(accumulate(nums[::-1]+[1], operator.mul))[::-1]+[1]
        #print(post)
        out = []
        for i in range(1, len(nums)+1):
            out.append(pre[i-1]*post[i+1])
        return out