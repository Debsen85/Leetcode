#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dashes = 0
        stack = []
        i = 0

        while i < len(traversal):
            if traversal[i] == '-':
                dashes += 1
                i += 1
            else:
                j = i

                while j < len(traversal) and traversal[j] != '-':
                    j += 1

                value = int(traversal[i : j])
                node = TreeNode(value)

                while stack and len(stack) > dashes:
                    stack.pop()

                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)

                i = j
                dashes = 0

        return stack[0]


# @lc code=end

