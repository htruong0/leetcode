from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if empty, return it back
        if not root:
            return root
        # invert left subtree
        self.invertTree(root.left)
        # invert right subtree
        self.invertTree(root.right)
        # swap them nodes/subtrees
        root.left, root.right = root.right, root.left
        return root
        