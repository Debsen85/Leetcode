#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def recursion(root):
            if not root:
                return 0

            answer = self.canSum(root, targetSum) 

            answer += recursion(root.left)
            answer += recursion(root.right)

            return answer
        
        return recursion(root)

    def canSum(self, root, targetSum):
        if not root:
            return 0

        count = 0

        if targetSum == root.val:
            count += 1

        count += self.canSum(root.left, targetSum - root.val) 
        count += self.canSum(root.right, targetSum - root.val)

        return count
        
# @lc code=end

