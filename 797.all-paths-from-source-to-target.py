#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        number = len(graph) - 1
        def backtracking(node, current):
            if node == number:
                answer.append(current[:])
                return 0
            if not current:
                current.append(node)
            for nextNode in graph[node]:
                current.append(nextNode)
                backtracking(nextNode, current)
                current.pop()
            return 0
        backtracking(0, [])
        return answer
# @lc code=end

