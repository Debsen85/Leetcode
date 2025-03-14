#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
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
            return False
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        for u, v in edges:
            if unionFind.union(u, v):
                return False
        return unionFind.getComponents() == 1
        
# @lc code=end

