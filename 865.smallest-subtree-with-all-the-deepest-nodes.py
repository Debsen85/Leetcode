#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        leftDepth, rightDepth = depth(root.left), depth(root.right)
        while leftDepth != rightDepth:
            if depth(root.left) > depth(root.right):
                root = root.left
            else:
                root = root.right
            leftDepth, rightDepth = depth(root.left), depth(root.right)

        return root
# @lc code=end

