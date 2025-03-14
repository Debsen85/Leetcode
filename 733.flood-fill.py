#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        queue = deque()
        Row = len(image)
        Col = len(image[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visited.add((sr, sc))
        queue.append((sr, sc))
        initialColor = image[sr][sc]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr >= 0 and nc >= 0 and nr < Row and nc < Col and image[nr][nc] == initialColor and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        return image
# @lc code=end

