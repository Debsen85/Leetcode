#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class FindElements:

    def __init__(self, root: Optional[TreeNode]): # type: ignore
        self.values = set()
        self.recover(root, 0)

    def recover(self, root, val):
        if not root:
            return
        
        self.values.add(val)
        root.val = val

        self.recover(root.left, 2 * val + 1)
        self.recover(root.right, 2 * val + 2)

        return

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

