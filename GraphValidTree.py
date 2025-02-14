from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.nodes = n
        self.components = n

        for i in range(self.nodes):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if (parentX != parentY):
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
                self.rank[parentX] += self.rank[parentY]
            else:
                self.parent[parentX] = parentY
                self.rank[parentY] += self.rank[parentX]
            self.components -= 1
            return False
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        for u, v in edges:
            if unionFind.union(u, v):
                return False
        return True if unionFind.components == 1 else False