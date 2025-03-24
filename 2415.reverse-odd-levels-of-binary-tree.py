#
# @lc app=leetcode id=2415 lang=python3
#
# [2415] Reverse Odd Levels of Binary Tree
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(r1, r2, position):
            if not r1 or not r2: return None
            if position % 2:
                r1.val, r2.val = r2.val, r1.val
            reverse(r1.left, r2.right, position + 1)
            reverse(r1.right, r2.left, position + 1)
        reverse(root.left, root.right, 1)
        return root
# @lc code=end

