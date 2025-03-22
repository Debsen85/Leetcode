#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [value for value in range(n)]
        self.rank = [1 for value in range(n)]
        self.indegree = [0 for value in range(n)]
        self.forest = [[value] for value in range(n)]
        self.component = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, X, Y):
        self.indegree[X] += 1
        self.indegree[Y] += 1
        self.forest[X].append(Y)
        self.forest[Y].append(X)
        x = self.find(X)
        y = self.find(Y)
        if x != y:
            if self.rank[y] <= self.rank[x]:
                self.parent[y] = self.parent[x]
                self.rank[x] += self.rank[y]
            else:
                self.parent[x] = self.parent[y]
                self.rank[y] += self.rank[x]
            #print(self.parent)
            self.component -= 1
            return False
        return True

    def getComponent(self):
        #print(self.component)
        return self.component

    def getForest(self):
        #print(self.forest)
        return self.forest

    def getIndegree(self):
        #print(self.indegree)
        return self.indegree
    
    def getRank(self):
        #print(self.rank)
        return self.rank

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for u, v in edges:
            unionFind.union(u, v)

        components = unionFind.getComponent()
        forest = unionFind.getForest()
        indegree = unionFind.getIndegree()
        rank = unionFind.getRank()

        for index, tree in enumerate(forest):
            if unionFind.find(index) == index:
                for vertices in tree:
                    if indegree[vertices] != rank[index] - 1:
                        components -= 1
                        break

        return components  
# @lc code=end

