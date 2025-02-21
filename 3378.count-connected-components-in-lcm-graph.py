#
# @lc app=leetcode id=3378 lang=python3
#
# [3378] Count Connected Components in LCM Graph
#

# @lc code=start
import math
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x):
        if x != self.parent[x]:
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
            self.components -= 1
            return False
        return True
    
    def getComponents(self):
        return self.components

class Solution:
    def gcd(self, a, b):
        if b % a == 0:
            return a
        return self.gcd(b % a, a)

    def lcm(self, a, b):
        return (a * b) // math.gcd(a, b)

    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        unionFind = UnionFind(n)
        nums = [num for num in nums if num <= threshold]
        indexMap = {num: i for i, num in enumerate(nums)}

        for num1 in range(1, threshold + 1):
            base = -1
            for num2 in range(num1, threshold + 1, num1):
                if num2 in indexMap:
                    if base == -1:
                        base = num2
                    elif self.lcm(base, num2) <= threshold:
                        unionFind.union(indexMap[base], indexMap[num2])

        return unionFind.getComponents()
# @lc code=end

