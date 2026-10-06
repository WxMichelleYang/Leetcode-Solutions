class TreeNode:
    def __init__(self, id=-1):
        self.id = id
        self.parent = -1
        self.children = set()

class Solution:
    def getRoot(self, node: TreeNode, nodes : List[TreeNode]) -> int:
        p = node
        while p.parent != p.id:
            # halv path
            p.parent = nodes[p.parent].parent 
            p = nodes[p.parent]
        return p.id
    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        ppls = [TreeNode(i) for i in range(n)]

        for p in ppls:
            p.parent = p.id

        sorted_logs =sorted(logs, key = lambda x:x[0])  
        usefuleEdges = 0
        for curTime, i1, i2 in sorted_logs:
            p1 = ppls[i1]
            p2 = ppls[i2]
            root1 = self.getRoot(p1, ppls)
            root2 = self.getRoot(p2, ppls)
            if root1 != root2:
                ppls[root2].parent = root1
                usefuleEdges += 1
                if usefuleEdges == n-1:
                    return curTime
        return -1        