#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Optional

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []

        def traverse(curr):
            if not curr:
                return 
            traverse(curr.left)
            inorder.append(curr)
            traverse(curr.right)
        
        traverse(root)
        size = len(inorder)

        for ind, num in enumerate(inorder):
            if num.val == p.val:
                if ind < (size - 1):
                    return inorder[ind + 1]
                else:
                    return None
        return None
# @lc code=end

