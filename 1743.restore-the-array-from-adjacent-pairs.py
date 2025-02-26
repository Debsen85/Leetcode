#
# @lc app=leetcode id=1743 lang=python3
#
# [1743] Restore the Array From Adjacent Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacentList = defaultdict(list)

        startNode = None
        self.answer = []

        for u, v in adjacentPairs:
            adjacentList[u].append(v)
            adjacentList[v].append(u)
        
        for key in adjacentList:
            if len(adjacentList[key]) == 1:
                startNode = key
                break

        def backtracking(node, visited):
            visited.add(node)

            if not self.answer:
                self.answer.append(node)

            for v in adjacentList[node]:
                if v not in visited:
                    self.answer.append(v)
                    backtracking(v, visited)

        backtracking(startNode, set())
        
        return self.answer

        
# @lc code=end

