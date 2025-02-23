#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = postorder.index(preorder[1])

        root.left = self.constructFromPrePost(preorder[1 : mid + 2], postorder[ : mid + 1])
        root.right = self.constructFromPrePost(preorder[mid + 2 : ], postorder[mid + 1 : len(postorder) - 1])

        return root
# @lc code=end

