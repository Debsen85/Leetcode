#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()
        time = 0

        for nr in range(rows):
            for nc in range(cols):
                if grid[nr][nc] == 2:
                    visit.add((nr, nc))
                    queue.append((nr, nc))

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visit and grid[r][c] == 1:
                        queue.append((r, c))
                        visit.add((r, c))             
            time += 1
        
        for nr in range(rows):
            for nc in range(cols):
                if grid[nr][nc] == 1 and (nr, nc) not in visit:
                        return -1
        return time - 1 if time > 0 else time
# @lc code=end

