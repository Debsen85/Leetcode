#
# @lc app=leetcode id=2924 lang=python3
#
# [2924] Find Champion II
#

# @lc code=start
from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        for u, v in edges:
            indegree[v] += 1
        m = min(indegree)
        if indegree.count(m) > 1:
            return -1
        for index, degree in enumerate(indegree):
            if degree == m:
                return index
        return -1
# @lc code=end

