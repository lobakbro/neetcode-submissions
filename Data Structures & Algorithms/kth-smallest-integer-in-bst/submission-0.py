# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.visited = 0
        def inorder(node) -> int | None:
            if not node:
                return None
            left= inorder(node.left)
            if left:
                return left
            self.visited += 1
            if self.visited == k:
                return node.val
            right=inorder(node.right)
            if right:
                return right
        return inorder(root)