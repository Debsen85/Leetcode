#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        visited = set()

        queue.append(tuple(entrance))
        visited.add(tuple(entrance))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        answer = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0) and (nc >= 0) and (nr < rows) and (nc < cols) and ((nr, nc) not in visited) and (maze[nr][nc] == "."):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        if ((nr == 0) or (nc == 0) or (nr == (rows - 1)) or (nc == (cols - 1))) and (maze[nr][nc] == "."):
                            return 1 + answer
            answer += 1
        return -1
# @lc code=end

