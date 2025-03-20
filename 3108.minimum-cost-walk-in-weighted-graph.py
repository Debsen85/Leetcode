#
# @lc app=leetcode id=3108 lang=python3
#
# [3108] Minimum Cost Walk in Weighted Graph
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [val for val in range(n)]
        self.rank = [1 for val in range(n)]
        self.component = n
        self.walk = {}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, w):
        X = self.find(x)
        Y = self.find(y)
        if X != Y:
            if X not in self.walk:
                self.walk[X] = w
            if Y not in self.walk:
                self.walk[Y] = w

            if self.rank[Y] <= self.rank[X]:
                self.parent[Y] = self.parent[X]
                self.rank[X] += self.rank[Y]
                self.walk[X] &= (self.walk[Y] & w)
            else:
                self.parent[X] = self.parent[Y]
                self.rank[Y] += self.rank[X]
                self.walk[Y] &= (self.walk[X] & w)
            self.component -= 1
        else:
            self.walk[X] &= w

    def getWalk(self, x):
        return self.walk[x]
    
    def getComponents(self):
        return self.component

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        unionFind = UnionFind(n)
        for u, v, w in edges:
            unionFind.union(u, v, w)
            
        answer = []

        for u, v in query:
            if unionFind.find(u) != unionFind.find(v):
                answer.append(-1)
            else:
                answer.append(unionFind.getWalk(unionFind.find(u)))

        return answer
        
# @lc code=end

