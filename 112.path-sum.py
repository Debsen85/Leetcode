#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def isPath(self, root, targetSum):
        if root == None:
            return False
        
        targetSum -= root.val

        if root.left == None and root.right == None:
                return targetSum == 0
            
        return self.isPath(root.left, targetSum) or self.isPath(root.right, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
       return self.isPath(root, targetSum)
        
# @lc code=end

