#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = [0]
        def backtracking(root, maxTillNow):
            if root == None:
                return
            if root.val >= maxTillNow:
                maxTillNow = root.val
                answer[0] += 1
            backtracking(root.right, maxTillNow)
            backtracking(root.left, maxTillNow)
        backtracking(root, root.val)
        return answer[0]
# @lc code=end

