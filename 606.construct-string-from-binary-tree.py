#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        def preorder(root):
            if not root: return None
            result.append(str(root.val))
            
            if root.left:
                result.append("(")
                preorder(root.left)
                result.append(")")
            else:
                if root.right:
                    result.append("()")

            if root.right:
                result.append("(")
                preorder(root.right)
                result.append(")")

        preorder(root)
        return "".join(result)

# @lc code=end

