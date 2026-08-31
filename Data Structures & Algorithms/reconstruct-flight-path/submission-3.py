from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m = defaultdict(list)
        tickets.sort()
        for t, f in tickets:
            m[t].append(f)

        out = ["JFK"]    
        
        def dfs(curr):
            if len(out) == len(tickets)+1: return True
            if curr not in m: return False
            temp = m[curr][:]
            for i, dst in enumerate(temp):
                out.append(dst)
                m[curr].pop(i)
                if dfs(dst): return True
                out.pop()
                m[curr].insert(i, dst)
                #m[curr] = temp
            return False
        dfs("JFK")
        return out