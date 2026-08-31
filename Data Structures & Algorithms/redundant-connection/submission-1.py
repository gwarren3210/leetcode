from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        for u,v in edges:
            m[u].append(v)
            m[v].append(u)
        cycle = set() # edge (u,v)
        visited = set()
        start = -1
        def dfs(node, prev):
            nonlocal start
            if node in visited:
                start = node
                return True
            visited.add(node)
            for nei in m[node]:
                if nei == prev: continue
                if dfs(nei, node): 
                    if start != -1:
                        cycle.add(node)
                    if node == start:
                        start = -1
                    return True
            return False

        dfs(1, -1)
        for u,v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u,v]
        
        return []