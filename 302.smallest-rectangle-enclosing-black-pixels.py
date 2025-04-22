#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        xVisited = set()
        yVisited = set()
        visited = set()
        queue = deque()

        ROW, COL = len(image), len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        xVisited.add(x)
        yVisited.add(y)
        visited.add((x, y))
        queue.append((x, y))

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr >= 0) and (nc >= 0) and (nr < ROW) and (nc < COL) and image[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        xVisited.add(nr)
                        yVisited.add(nc)
                        queue.append((nr, nc))
        
        return len(xVisited) * len(yVisited)
# @lc code=end

