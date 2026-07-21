# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.in_dict = {}
        out_tree = None
        self.index = 0
        for n, val in enumerate(inorder):
            self.in_dict[val] = n

        self.preorder_index = 0
        self.preorder = preorder
        def build(left,right)->Optional[TreeNode]:
            if left > right:
                return None
            index = self.preorder_index
            self.preorder_index +=1
            root = TreeNode(self.preorder[index])
            mid = self.in_dict.get(root.val)
            root.left = build(left, mid-1)
            root.right = build(mid+1, right)
            return root
        
        return build(0, len(inorder)-1)
            