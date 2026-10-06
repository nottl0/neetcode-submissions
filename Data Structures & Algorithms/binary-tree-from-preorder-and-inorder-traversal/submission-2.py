# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = preorder[0]
        print(root)
        print(preorder)
        print(inorder)
        div = inorder.index(root)
        ind_in_preorder = div
        
        rootNode = TreeNode(val=root)
        rootNode.left = self.buildTree(preorder[1:ind_in_preorder+1], inorder[:div])
        rootNode.right = self.buildTree(preorder[ind_in_preorder+1:], inorder[div+1:])
        return rootNode