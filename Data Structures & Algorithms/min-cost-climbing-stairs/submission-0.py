class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            #print(i,": ", dp, sep="")
            n = min(dp) + cost[i]
            dp = [dp[1], n]
            #dpd.append(n)
        #print(dp)
        #print(cost)
        #print(dpd)
        return min(dp)