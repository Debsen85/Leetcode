#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        minHeap = []
        result = {}
        adjacencyList = defaultdict(list)
        for index in range(len(edges)):
            adjacencyList[edges[index][0]].append((succProb[index], edges[index][1]))
            adjacencyList[edges[index][1]].append((succProb[index], edges[index][0]))
        heappush(minHeap, (-1.0, start_node))
        while minHeap:
            currProb, currNode = heappop(minHeap)
            currProb = -currProb
            if currNode in result:
                continue
            result[currNode] = currProb
            for prob, node in adjacencyList[currNode]:
                if node not in result:
                    heappush(minHeap, (-(currProb * prob), node))
        return result[end_node] if end_node in result else 0.0
# @lc code=end

