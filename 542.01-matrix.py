#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visit = set()
        queue = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        Row, Col = len(mat), len(mat[0])

        for row in range(Row):
            for col in range(Col):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visit.add((row, col))

        level = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if mat[r][c] > 0:
                    mat[r][c] = level
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr >= 0 and nc >= 0 and nr < Row and nc < Col and (nr, nc) not in visit:
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            level += 1
        return mat
# @lc code=end

