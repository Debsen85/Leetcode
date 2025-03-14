#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.components = n

    def getComponents(self):
        return self.components

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        X = self.find(x)
        Y = self.find(y)

        if (X != Y):
            if self.rank[X] > self.rank[Y]:
                self.parent[Y] = self.parent[X]
                self.rank[X] += self.rank[Y]
            else:
                self.parent[X] = self.parent[Y]
                self.rank[Y] += self.rank[X]
            self.components -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for u, v in edges:
            unionFind.union(u, v)
        return unionFind.getComponents()

# @lc code=end

