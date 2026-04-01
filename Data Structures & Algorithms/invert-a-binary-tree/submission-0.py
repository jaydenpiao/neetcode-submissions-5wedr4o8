# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        given root of binary tree and goal is to invert and return root

        i think the idea is to go all the way to the children, then invert recursively

        so go all the way down to 4, since its leaf, or base case, we invert

        so we need to do a dfs
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root