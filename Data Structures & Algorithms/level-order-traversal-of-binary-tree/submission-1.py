# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while len(q) != 0:
            curr = []
            while len(q) != 0:
                curr.append(q.popleft())
            ans.append([node.val for node in curr])
            i = 0
            while i < len(curr):
                if curr[i].left:
                    q.append(curr[i].left)
                if curr[i].right:
                    q.append(curr[i].right)
                i += 1
        return ans
            

