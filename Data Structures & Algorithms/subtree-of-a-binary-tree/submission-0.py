# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root, subRoot) -> bool:
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:    
                return isEqual(root.right, subRoot.right) and isEqual(root.left, subRoot.left)
            else:
                return False
        if root is None:
            return False
        if isEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
