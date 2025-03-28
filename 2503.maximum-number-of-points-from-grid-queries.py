#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        cache = {}
        answer = []
        queue = []
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        copyQueries = sorted(list(set(queries)))

        def breadthFirstSearch():
            heapq.heapify(queue)
            visited = set()
            total = 0
            visited.add((0, 0))
            heapq.heappush(queue, (grid[0][0], 0, 0))

            for query in copyQueries:
                while queue and queue[0][0] < query:
                    total += 1
                    _, r, c = heapq.heappop(queue)
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if (nr >= 0) and (nc >= 0) and (nr < ROW) and (nc < COL) and (nr, nc) not in visited:
                            heapq.heappush(queue, (grid[nr][nc], nr, nc))
                            visited.add((nr, nc))
                cache[query] = total

        breadthFirstSearch()

        for query in queries:
            answer.append(cache[query])

        return answer
        
# @lc code=end

