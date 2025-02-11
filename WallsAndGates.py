from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def breadthFirstSearch(row, col):
            queue = deque()
            visited = set()
            queue.append((row, col))
            visited.add((row, col))
            distance = 0
            while queue:
                distance += 1
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr >= 0 and nr < ROW and nc >= 0 and nc < COL and grid[nr][nc] != -1 and (nr, nc) not in visited:
                            if grid[nr][nc] != 0:
                                grid[nr][nc] = min(grid[nr][nc], distance)
                            visited.add((nr, nc))
                            queue.append((nr, nc))

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    breadthFirstSearch(i, j)