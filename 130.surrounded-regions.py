#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        region = 1
        hashMap = {}

        def breadthFirstSearch(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            surrounded = True

            while queue:
                row, col = queue.popleft()
                board[row][col] = str(region)
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < ROW and nc >= 0 and nc < COL and board[nr][nc] != "X" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                    else:
                        if min(nr, nc) < 0 or nr == ROW or nc == COL:
                            surrounded = False
            
            hashMap[str(region)] = surrounded
                    

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r, c) not in visited:
                    breadthFirstSearch(r, c)
                    region += 1

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != "X":
                    if hashMap[board[r][c]]:
                        board[r][c] = "X"
                    else:
                        board[r][c] = "O"
        
        
# @lc code=end

