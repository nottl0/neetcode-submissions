# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        def dfs(node):
            if node is None:
                return 
            heapq.heappush(heap, node.val)
            dfs(node.left) 
            dfs(node.right)
        dfs(root)

        while k > 0:
            val = heapq.heappop(heap)
            k -= 1
        return val


