class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1
        tg = 0
        tc = 0
        s = 0
        for i in range(len(cost)):
            tg += gas[i]
            tc += cost[i]
            if tc > tg:
                s = i+1
                tc  = 0
                tg = 0
        return s
        # see if you can go backwards from the end