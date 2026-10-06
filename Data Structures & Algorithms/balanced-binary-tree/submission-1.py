# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def find_depth(self, root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            left_depth = find_depth(self, root.left) + 1
            right_depth = find_depth(self, root.right) + 1
            
            if abs(left_depth - right_depth) <= 1:
                self.is_balanced = self.is_balanced
            else:
                self.is_balanced = False
            return max(left_depth, right_depth)
        find_depth(self, root)
        return self.is_balanced
            
        
        
        