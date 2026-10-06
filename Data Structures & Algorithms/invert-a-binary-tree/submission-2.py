# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapChilds(root: Optional[TreeNode]):
            if root:
                root.left, root.right = root.right, root.left

        swapChilds(root)
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root