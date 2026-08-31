class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        prof = 0
        bought = prices[0]
        for p in prices[1:]:
            if p > bought:
                prof += p-bought
            bought = p
        return prof