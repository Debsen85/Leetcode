#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def distance(self, x, y):
        return (x ** 2 + y ** 2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = defaultdict(list)
        a = []
        for point in points:
            d[self.distance(point[0], point[1])].append(point)

        point = list(d.keys())
        heapq.heapify(point)
        while k > 0:
            v = heapq.heappop(point)
            a.extend(d[v][ : min(len(d[v]), k)])
            k -= min(len(d[v]), k)
        
        return a
            
# @lc code=end

