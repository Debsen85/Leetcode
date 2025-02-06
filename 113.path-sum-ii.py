#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []

        def isPath(root, targetSum, path):
            if root == None:
                return
            
            targetSum -= root.val
            path.append(root.val)

            if root.left == None and root.right == None and targetSum == 0:
                answer.append(path[:])
            
            isPath(root.left, targetSum, path)
            isPath(root.right, targetSum, path)

            path.pop()

        isPath(root, targetSum, [])
        return answer
        
# @lc code=end

