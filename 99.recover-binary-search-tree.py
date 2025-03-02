#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        elements = []   
        def backtracking(current):
            if not current:
                return None
            backtracking(current.left)
            elements.append(current)
            backtracking(current.right)
        backtracking(root)
        nums = sorted(elements, key=lambda x: x.val)
        for i in range(len(nums)):
            if nums[i].val != elements[i].val:
                elements[i].val, nums[i].val = nums[i].val, elements[i].val
                break
        
# @lc code=end

