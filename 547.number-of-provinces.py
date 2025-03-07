#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.component = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = self.parent[parentX]
                self.rank[parentX] += self.rank[parentY]
            else:
                self.parent[parentX] = self.parent[parentY]
                self.rank[parentY] += self.rank[parentX]
            self.component -= 1
    
    def getComponents(self):
        return self.component

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = []

        for r in range(len(isConnected)):
            for c in range(r + 1, len(isConnected[0])):
                if isConnected[r][c] and r != c:
                    edges.append([r, c])

        unionFind = UnionFind(len(isConnected))

        for r, c in edges:
            unionFind.union(r, c)

        return unionFind.getComponents()
# @lc code=end

