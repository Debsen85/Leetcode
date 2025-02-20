#
# @lc app=leetcode id=1861 lang=python3
#
# [1861] Rotating the Box
#

# @lc code=start
from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROW, COL = len(boxGrid), len(boxGrid[0])
        for r in range(ROW):
            i, j = 0, 0
            while j < COL:
                if boxGrid[r][j] == "*":
                    i, j = j + 1, j + 1
                elif boxGrid[r][j] == ".":
                    boxGrid[r][i], boxGrid[r][j] = boxGrid[r][j], boxGrid[r][i]
                    i += 1
                    j += 1
                else:
                    j += 1
        answer = [[0] * ROW for _ in range(COL)]
        for r in range(ROW):
            for c in range(COL):
                answer[c][ROW - r - 1] = boxGrid[r][c]
        return answer
# @lc code=end

