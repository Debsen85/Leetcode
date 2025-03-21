#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
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
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        def getValues(root):
            if not root: return None
            getValues(root.left)
            values.append(root.val)
            getValues(root.right)
        getValues(root)
        def buildTree(index):
            if index == len(values): return None
            root = TreeNode(values[index])
            root.right = buildTree(index + 1)
            return root
        return buildTree(0)
# @lc code=end

