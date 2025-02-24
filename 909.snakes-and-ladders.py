#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def check(self, number, ROW):
        row = ROW - 1 - ((number - 1) // ROW)
        if ROW % 2:
            if row % 2:
                return [row, ROW - 1 - ((number - 1) % ROW)]
            else:
                return [row, ((number - 1) % ROW)]
        else:
            if row % 2:
                return [row, ((number - 1) % ROW)]
            else:
                return [row, ROW - 1 - ((number - 1) % ROW)]
                
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ROW = len(board)
        TOTAL = ROW * ROW

        queue = deque()
        visited = set()

        queue.append(1)
        visited.add((ROW - 1, 0))

        answer = 0

        while queue:
            for _ in range(len(queue)):
                value = queue.popleft()
                if value == TOTAL:
                    return answer
                for change in range(1, 7):
                    if (value + change) > TOTAL:
                        break
                    row, col = self.check(value + change, ROW)
                    if (row, col) not in visited:
                        if board[row][col] == -1:
                            queue.append(value + change)
                        else:
                            queue.append(board[row][col])
                        visited.add((row, col))
            answer += 1
        return -1
# @lc code=end

