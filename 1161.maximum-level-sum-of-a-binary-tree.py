#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        answer = float("-inf")
        result = 1
        level = 1

        queue.append(root)

        while queue:
            levelSum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelSum > answer:
                answer = levelSum
                result = level

            level += 1

        return result 
        
# @lc code=end

