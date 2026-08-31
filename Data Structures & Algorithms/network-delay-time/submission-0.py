import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = collections.defaultdict(lambda: float('inf'))
        m = collections.defaultdict(list) # source: (time, target)
        # weighted bfs meaning the queue will be a min heap and not a q
        for ui, vi, ti in times:
            m[ui].append((ti,vi))
        heap = m[k]
        seen[k] = 0
        heapq.heapify(heap)
        while heap:
            #print("heap", heap)
            time, node = heapq.heappop(heap)
            if seen[node] <= time: continue
            seen[node] = time
            for tm, tg in m[node]:
                heapq.heappush(heap, (tm+time, tg))
        #print(seen.values())
        return max(seen.values()) if len(seen) == n else -1