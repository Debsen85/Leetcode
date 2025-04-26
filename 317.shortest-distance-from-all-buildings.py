#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        totalBuildings = 0
        cache = [[0 for _ in range(COL)] for _ in range(ROW)]
        visited = [[0 for _ in range(COL)] for _ in range(ROW)]
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def possiblePath(row, col):
            queue = deque()
            visit = set()
            queue.append((row, col))
            visit.add((row, col))
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if r != row or c != col:
                        cache[r][c] += distance
                        visited[r][c] += 1
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if (nr >= 0) and (nc >= 0) and (nr < ROW) and (nc < COL) and ((nr, nc) not in visit) and grid[nr][nc] == 0:
                            queue.append((nr, nc))
                            visit.add((nr, nc))
                distance += 1

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    totalBuildings += 1
                    possiblePath(row, col)    

        answer = float("inf")    

        for row in range(ROW):
            for col in range(COL):
                if totalBuildings == visited[row][col]:
                    answer = min(cache[row][col], answer)
        
        return answer if answer != float("inf") else -1
# @lc code=end

