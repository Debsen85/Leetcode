#
# @lc app=leetcode id=2737 lang=python3
#
# [2737] Find the Closest Marked Node
#

# @lc code=start
from cmath import inf
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        hs = defaultdict(set)

        for i, j, v in edges:
            hs[i].add((j, v))
        
        heap = []
        heapq.heappush(heap, (0, s))
        mn = inf
        seen = defaultdict(int)

        while heap:

            w, n = heapq.heappop(heap)
        
            if n in marked:
                mn = min(mn, w)
                continue
            
            for nd, we in hs[n]:
                if nd in seen:
                    if seen[nd] < we + w:
                        continue
                    else:
                        seen[nd] = we + w
                else:
                    seen[nd] = we + w
                if nd in marked:
                    mn = min(mn, we + w)
                heapq.heappush(heap, (w + we, nd))

        return mn if mn != inf else -1
# @lc code=end

