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
        level, answer = 0, 0
        maxTotal = float("-inf")
        queue = deque()
        queue.append(root)

        while queue:
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1  
            if total > maxTotal:
                answer = level
                maxTotal = total
        
        return answer
        
# @lc code=end

