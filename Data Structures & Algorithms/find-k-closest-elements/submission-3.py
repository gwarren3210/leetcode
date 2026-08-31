from bisect import bisect_left, bisect_right
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr): return arr
        l = bisect_left(arr, x)
        if l == 0: return arr[:k]
        r = bisect_right(arr, x)
        if r == len(arr): return arr[r-k:]
        if r-l >= k: return [x]*k
        out = [x]*(r-l)
        l-=1
        while len(out)<k:
            if (r<len(arr) and abs(arr[r]-x) < abs(arr[l]-x)) or l<0:
                out.append(arr[r])
                r +=1
            else:
                out = [arr[l]]+out[:]
                l -=1
        return out