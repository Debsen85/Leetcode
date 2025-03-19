#
# @lc app=leetcode id=789 lang=python3
#
# [789] Escape The Ghosts
#

# @lc code=start
from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myPath = abs(target[0]) + abs(target[1])
        ghostPath = float("inf")
        for ghost in ghosts:
            ghostPath = min(ghostPath, abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))
        return myPath < ghostPath
# @lc code=end

