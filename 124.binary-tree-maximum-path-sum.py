#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        def backtrack(node):
            if not node:
                return 0

            leftSum = max(backtrack(node.left), 0)
            rightSum = max(backtrack(node.right), 0)

            self.result = max(self.result, leftSum + rightSum + node.val)

            return node.val + max(leftSum, rightSum)
        
        backtrack(root)
        return self.result
# @lc code=end

