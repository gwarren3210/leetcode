class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = { i:[] for i in range(n) }
        for i, e in edges:
            m[i].append(e)
            m[e].append(i)

        visited = set()
        seen = set()

        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in m[node]:
                if nei == par: continue
                if not dfs(nei, node): return False
            return True

        return dfs(0, -1) and len(visited) == n