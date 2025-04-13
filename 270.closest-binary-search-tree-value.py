#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.answer = float("inf")
        self.diff = float("inf")
        def depthFirstSearch(node):
            if not node:
                return 0
            if node.val >= target:
                if self.diff > abs(target - node.val):
                    self.answer = node.val
                    self.diff = abs(target - node.val)
                elif self.diff == abs(target - node.val):
                    self.answer = min(node.val, self.answer)
                    self.diff = abs(target - node.val)
                depthFirstSearch(node.left)
            else:
                if self.diff > abs(target - node.val):
                    self.answer = node.val
                    self.diff = abs(target - node.val)
                elif self.diff == abs(target - node.val):
                    self.answer = min(node.val, self.answer)
                    self.diff = abs(target - node.val)
                depthFirstSearch(node.right)
        depthFirstSearch(root)
        return self.answer
# @lc code=end

