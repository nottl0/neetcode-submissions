# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGood = 0
        def isGood(node, maxVal):
            nonlocal numGood
            if not node:
                return
            if node.val >= maxVal:
                numGood += 1
                maxVal = node.val
            isGood(node.left, maxVal)
            isGood(node.right, maxVal)
        isGood(root, root.val)
        return numGood
            

