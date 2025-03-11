#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashMap = defaultdict(list)
        def traversal(curr, pos, level):
            if not curr:
                return None

            hashMap[pos].append((level, curr.val))

            traversal(curr.left, pos - 1, level + 1)
            traversal(curr.right, pos + 1, level + 1)

        traversal(root, 0, 1)
        answer = []
        keyList = list(hashMap.keys())
        keyList.sort()
        for key in keyList:
            hashMap[key].sort(key=lambda x: x[0])
            new = []
            for k in hashMap[key]:
                new.append(k[1])
            answer.append(new)
        return answer
# @lc code=end

