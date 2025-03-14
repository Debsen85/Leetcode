#
# @lc app=leetcode id=2658 lang=python3
#
# [2658] Maximum Number of Fish in a Grid
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        Row = len(grid)
        Col = len(grid[0])
        answer = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def getTotalFish(row, col):
            visited.add((row, col))
            queue.append((row, col))
            total = 0

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    total += grid[r][c]
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if nr >= 0 and nr < Row and nc >= 0 and nc < Col and grid[nr][nc] > 0 and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            return total
        
        for row in range(Row):
            for col in range(Col):
                if grid[row][col] > 0 and (row, col) not in visited:
                    answer = max(answer, getTotalFish(row, col))
        
        return answer
# @lc code=end

