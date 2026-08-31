# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []
        def dfs(n):
            if n == None:
                out.append("N")
                return
            out.append(str(n.val))
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return ','.join(out)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        i = [0]
        def dfs():
            if data[i[0]] == "N":
                i[0] += 1
                return None
            n = TreeNode(int(data[i[0]]))
            i[0] += 1
            n.left = dfs()
            n.right = dfs()
            return n
        return dfs()