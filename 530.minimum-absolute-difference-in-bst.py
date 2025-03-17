#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        answer = float("inf")
        for index in range(1, len(nums)):
            answer = min(answer, nums[index] - nums[index - 1])
        return answer
# @lc code=end

