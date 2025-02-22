#
# @lc app=leetcode id=1197 lang=python3
#
# [1197] Minimum Knight Moves
#

# @lc code=start
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0: return 0
        directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        visited = set()
        queue = deque()
        
        visited.add((0, 0))
        queue.append((0, 0))
        answer = 1
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr == x and nc == y:
                        return answer
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            answer += 1
        return 0    
# @lc code=end

