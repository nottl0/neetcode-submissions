# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order = []
        self.stack = []
        if root is not None:
            self.stack.append([root])
        while len(self.stack) != 0:
            nextLevel = []
            currValues = []
            currLevel = self.stack.pop()
            for node in currLevel:
                currValues.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel != []:
                self.stack.append(nextLevel)
            self.order.append(currValues)
        return self.order
