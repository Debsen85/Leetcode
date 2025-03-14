#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        elements = []

        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            elements.append(node.val)
            inorder(node.right)
        
        inorder(root)

        for index in range(1, len(elements)):
            if elements[index] <= elements[index - 1]:
                return False
        return True
# @lc code=end

