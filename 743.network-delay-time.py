#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        result = {}
        adjacencyList = defaultdict(list)
        for u, v, t in times:
            adjacencyList[u].append((t, v))
        heappush(minHeap, (0, k))
        while minHeap:
            currTime, currNode = heappop(minHeap)
            if currNode in result:
                continue
            result[currNode] = currTime
            for nextTime, nextNode in adjacencyList[currNode]:
                if nextNode not in result:
                    heappush(minHeap, (nextTime + currTime, nextNode))
        answer = 0
        for node in range(1, n + 1):
            if node not in result:
                return -1
            answer = max(answer, result[node])
        return answer
# @lc code=end

