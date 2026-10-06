# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.is_same = True
        def check_nodes(self, p: Optional[TreeNode], q: Optional[TreeNode]):
            if p == None:
                if q != None:
                    self.is_same = False
                return 
            if q == None:
                if p != None:
                    self.is_same = False
                return 
            if p.val != q.val:
                self.is_same = False
            check_nodes(self, p.left, q.left)
            check_nodes(self, p.right, q.right)
            return
        check_nodes(self, p, q)
        return self.is_same