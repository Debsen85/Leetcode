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

        def backtrackingForBob(current, listBob):
            if current == bob:
                self.pathBob = listBob[:]
                return

            for v in adjacencyList[current]:
                listBob.append(v)
                backtrackingForBob(v, listBob)
                listBob.pop()

        backtrackingForBob(0, [0])
        
        self.pathBob = self.pathBob[::-1]
        visitedBob = set(self.pathBob)
        adjacencyList = [[] for _ in range(len(edges) + 1)]

        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        def backtrackingForAlice(alice, turn, visitedAlice):
            if alice in visitedAlice:
                return  -(10 ** 9 + 1)
            result = 0
            if alice in visitedBob:
                if turn == 0:
                    result = amount[alice]
                elif turn < len(self.pathBob):
                    if self.pathBob[turn] == alice:
                        result = amount[alice] // 2
                    elif alice < self.pathBob[turn]:
                        result = amount[alice]
            else:
                result = amount[alice]

            visitedAlice.add(alice)
            
            print(alice, result)

            maxSum = -(10 ** 9 + 1)
            for v in adjacencyList[alice]:
                maxSum = max(maxSum, backtrackingForAlice(v, turn + 1, visitedAlice))

            return result + (maxSum if maxSum != -(10 ** 9 + 1) else 0)
        
        return backtrackingForAlice(0, 0, set())
            
# @lc code=end

