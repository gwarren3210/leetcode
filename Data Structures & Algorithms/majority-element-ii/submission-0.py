class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = {} #(key, count)
        for n in nums:
            if n in m:
                m[n] += 1
            elif len(m)<2:
                m[n] = 1
            else:
                keys = list(m.keys())
                for k in keys:
                    m[k] -= 1
                    if m[k] == 0:
                        del m[k]
        out = []
        for k in m.keys():
            if nums.count(k) > len(nums)//3:
                out.append(k)
        
        return out