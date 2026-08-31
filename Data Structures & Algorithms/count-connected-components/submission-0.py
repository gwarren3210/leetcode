class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = { i:[] for i in range(n) }
        for u, v in edges:
            m[u].append(v)
            m[v].append(u)
         
        visited = set()
        out = 0

        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nei in m[node]:
                dfs(nei)
        
        for i in range(n):
            if i in visited: continue
            out += 1
            dfs(i)
        
        return out