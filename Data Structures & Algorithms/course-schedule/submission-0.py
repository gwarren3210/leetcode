class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = { i:[] for i in range(numCourses) }
        for crs, p in prerequisites:
            m[crs].append(p)
        
        visited = set()

        def dfs(c):
            if c in visited: return False
            if m[c] == []: return True
            visited.add(c)
            for cs in m[c]:
                if not dfs(cs): return False
            visited.remove(c)
            m[c] = []
            return True

        for i in m.keys():
            if not dfs(i): return False
        
        return True