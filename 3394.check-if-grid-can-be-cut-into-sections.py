#
# @lc app=leetcode id=3394 lang=python3
#
# [3394] Check if Grid can be Cut into Sections
#

# @lc code=start
from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        h = []
        v = []
        for a, b, c, d in rectangles:
            h.append([b, d])
            v.append([a, c])
        h.sort()
        v.sort()
        ans1 = []
        ans2 = []
        for index in range(1, len(h)):
            if h[index][0] < h[index - 1][1]:
                h[index][0] = min(h[index][0], h[index - 1][0])
                h[index][1] = max(h[index][1], h[index - 1][1])
            else:
                ans1.append([h[index - 1][0], h[index - 1][1]])
                if len(ans1) == 2:
                    return True
        ans1.append([h[-1][0], h[-1][1]])
        
        for index in range(1, len(v)):
            if v[index][0] < v[index - 1][1]:
                v[index][0] = min(v[index][0], v[index - 1][0])
                v[index][1] = max(v[index][1], v[index - 1][1])
            else:
                ans2.append([v[index - 1][0], v[index - 1][1]])
                if len(ans2) == 2:
                    return True
        ans2.append([v[-1][0], v[-1][1]])

        return len(ans1) >= 3 or len(ans2) >= 3
# @lc code=end

