#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque
from typing import List

# class UnionFind:
#     def __init__(self, n):
#         self.parent = {}
#         self.rank = {}

#         for i in range(n):
#             self.parent[i] = i
#             self.rank[i] = 1

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         parentX = self.find(x)
#         parentY = self.find(y)
#         if parentX != parentY:
#             if self.rank[parentX] < self.rank[parentY]:
#                 self.parent[parentX] = parentY
#                 self.rank[parentY] += self.rank[parentX]
#             else:
#                 self.parent[parentY] = parentX
#                 self.rank[parentX] += self.rank[parentY]
#             print("True", self.parent, self.rank)
#             return True
#         print("False", self.parent, self.rank)
#         return False

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            courseMap[course].append(prerequisite)

        visited, cycle = set(), set()
        answer = []

        def travel(index):
            if index in cycle:
                return False
            if index in visited:
                return True
            cycle.add(index)

            for course in courseMap[index]:
                if not travel(course):
                    return False
                
            cycle.remove(index)
            visited.add(index)
            answer.append(index)
            return True

        for index in range(numCourses):
            if not travel(index):
                return []
            
        return answer
    # @lc code=end

