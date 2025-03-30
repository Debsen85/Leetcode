#
# @lc app=leetcode id=2737 lang=python3
#
# [2737] Find the Closest Marked Node
#

# @lc code=start
from math import inf
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        minHeap = []
        result = {}
        adjacencyList = defaultdict(list)
        for u, v, w in edges:
            adjacencyList[u].append((w, v))
        heapq.heappush(minHeap, (0, s))
        while minHeap:
            currWeight, currNode = heapq.heappop(minHeap)
            if currNode in result:
                continue
            result[currNode] = currWeight
            for weight, node in adjacencyList[currNode]:
                if node not in result:
                    heapq.heappush(minHeap, (weight + currWeight, node))
        answer = float("inf")
        for mark in marked:
            if mark in result:
                answer = min(answer, result[mark])
        return answer if answer != float("inf") else -1
# @lc code=end

