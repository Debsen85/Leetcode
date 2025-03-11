#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
from typing import Optional

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        queue = deque()
        queue.append(root)
        
        while (queue):
            temp = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if temp:
                    temp.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp = node
            temp.next = None
        return root
        
# @lc code=end

