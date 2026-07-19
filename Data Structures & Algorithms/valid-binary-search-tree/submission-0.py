# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        def inorder(node) -> bool:
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val > self.prev:
                self.prev= node.val
            else:
                return False
            if not inorder(node.right):
                return False
            return True
            
    
        return inorder(root)