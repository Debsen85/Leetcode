#
# @lc app=leetcode id=3208 lang=python3
#
# [3208] Alternating Groups II
#

# @lc code=start
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        output = 0
        colors += colors[ : k - 1]
        i, j = 0,  1
        while j < len(colors):
            if colors[j] == colors[j - 1]:
                i = j
            
            if j - i + 1 > k:
                i += 1
            
            if j - i + 1 == k:
                output += 1
            
            j += 1
        
        return output
# @lc code=end

