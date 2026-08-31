class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l = prices[0] if prices else 0
        for p in prices[1:]:
            m = max(m, p-l)
            l = min(l, p)
        return m