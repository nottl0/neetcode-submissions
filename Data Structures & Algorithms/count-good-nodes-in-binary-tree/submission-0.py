# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        totalGood = 1
        def isGood(root, prevmax):
            nonlocal totalGood
            if not root:
                return 
            if root.val >= prevmax:
                totalGood += 1
                prevmax = root.val
            isGood(root.left, prevmax)
            isGood(root.right, prevmax)
        isGood(root.left, root.val)
        isGood(root.right, root.val)
        return totalGood