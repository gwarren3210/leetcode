class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = { i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            m[c].append(p)

        visited = set()
        inOut = set()
        out = []

        def dfs(crs):
            if crs in visited: return False
            if crs in inOut: return True
            
            visited.add(crs)

            for c in m[crs]:
                if not dfs(c): return False
            
            visited.remove(crs)
            out.append(crs)
            inOut.add(crs)
            m[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return out