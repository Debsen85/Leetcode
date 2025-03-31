#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjacentList = defaultdict(list)
        minHeap = []
        mod = 10 ** 9 + 7
        pathCount = [0] * n
        pathCost = [float("inf")] * n
        for u, v, w in roads:
            adjacentList[u].append((w, v))
            adjacentList[v].append((w, u))
        heappush(minHeap, (0, 0))
        pathCount[0] = 1
        while minHeap:
            currCost, currNode = heappop(minHeap)
            for cost, node in adjacentList[currNode]:
                if currCost + cost < pathCost[node]:
                    pathCost[node] = currCost + cost
                    pathCount[node] = pathCount[currNode]
                    heappush(minHeap, (currCost + cost, node))
                elif currCost + cost == pathCost[node]:
                    pathCount[node] = (pathCount[node] + pathCount[currNode]) % mod
        return pathCount[-1]
        
# @lc code=end

