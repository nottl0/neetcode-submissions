"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}
        def dfs(node):
            if node is None:
                return
            if node.val in created:
                currNode = created[node.val]
            else:
                currNode = Node(val=node.val)
            created[node.val] = currNode
            currNeighbors = []
            for n in node.neighbors:
                if n.val in created:
                    currNeighbors.append(created[n.val])
                else:
                    newNode = Node(val=n.val)
                    created[n.val] = newNode
                    dfs(n)
                    currNeighbors.append(newNode)
            
            currNode.neighbors = currNeighbors
            
     
        dfs(node)
        if len(created)==0:
            return None
        return created[1]

            





