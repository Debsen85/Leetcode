#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        atlantic = set()
        pacific = set()

        def travel(row, col, flow):
            queue = deque()
            queue.append((row, col))
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if "A" in flow:
                        atlantic.add((r, c))
                    if "P" in flow:
                        pacific.add((r, c))
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and heights[r][c] <= heights[nr][nc]:
                            if flow == "A" and (nr, nc) not in atlantic:
                                atlantic.add((nr, nc))
                                queue.append((nr, nc))
                            elif flow == "P" and (nr, nc) not in pacific:
                                pacific.add((nr, nc))
                                queue.append((nr, nc))
                            elif flow == "AP" and ((nr, nc) not in atlantic or (nr, nc) not in pacific):
                                atlantic.add((nr, nc))
                                pacific.add((nr, nc))
                                queue.append((nr, nc))
        for r in range(ROWS):
            if r == ROWS - 1:
                travel(r, 0, "AP")
            else:
                travel(r, 0, "P")
            if r == 0:
                travel(r, COLS - 1, "AP")
            else:
                travel(r, COLS - 1, "A")
        
        for c in range(1, COLS - 1):
            travel(0, c, "P")
            travel(ROWS - 1, c, "A")
        return sorted(list(atlantic.intersection(pacific)))
# @lc code=end

