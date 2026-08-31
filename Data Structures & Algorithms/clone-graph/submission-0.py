"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        m = {}
        temp = node
        m[node] = Node(temp.val, [])
        q = [node]
        while q:
            temp = q.pop()
            for n in temp.neighbors:
                if n not in m:
                    m[n] = Node(n.val, [])
                    q.append(n)
                m[temp].neighbors.append(m[n])
        return m[node]
