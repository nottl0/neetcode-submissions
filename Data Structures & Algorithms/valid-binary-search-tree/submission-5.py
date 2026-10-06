# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(left, root, right):
            if not root:
                return True
            elif not left.val < root.val < right.val:
                return False
            else:
                return isValid(left, root.left, root) and isValid(root, root.right, right)
        return isValid(TreeNode(val=float("-inf")), root, TreeNode(val=float("inf")))

