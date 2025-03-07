#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, []) == self.dfs(root2, [])

    def dfs(self, root, value):
        if not root:
            return None

        if not root.left and not root.right:
            value.append(root.val)

        self.dfs(root.left, value)
        self.dfs(root.right, value)

        return value
# @lc code=end

