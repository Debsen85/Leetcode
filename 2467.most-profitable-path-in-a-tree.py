#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjacencyList = [[] for _ in range(len(edges) + 1)]
        self.pathBob = []

        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        def backtrackingForBob(current, listBob, visitedBob):
            if current in visitedBob:
                return
            if current == bob:
                self.pathBob = listBob[:]
                return
            if current == 0:
                listBob.append(0)
            visitedBob.add(current)

            for v in adjacencyList[current]:
                listBob.append(v)
                backtrackingForBob(v, listBob, visitedBob)
                listBob.pop()
            
            return

        backtrackingForBob(0, [], set())
        self.pathBob = self.pathBob[::-1]

        def backtrackingForAlice(alice, turn, visitedAlice, visitedBob):
            if alice in visitedAlice:
                return  -(10 ** 9 + 1)

            result = 0
            
            if turn < len(self.pathBob):
                if alice not in visitedBob:
                    if alice == self.pathBob[turn]:
                        result = amount[alice] // 2
                    else:
                        result = amount[alice]
            else:
                if alice not in visitedBob:
                    result = amount[alice]

            maxSum = -(10 ** 9 + 1)
            for v in adjacencyList[alice]:
                if turn < len(self.pathBob):
                    visitedBob.add(self.pathBob[turn])
                visitedAlice.add(alice)
                maxSum = max(maxSum, backtrackingForAlice(v, turn + 1, visitedAlice, visitedBob))
                if turn < len(self.pathBob):
                    visitedBob.remove(self.pathBob[turn])
                visitedAlice.remove(alice)

            return result + (maxSum if maxSum != -(10 ** 9 + 1) else 0)
        
        return backtrackingForAlice(0, 0, set(), set())
            
# @lc code=end

