#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = senate.count('D')
        R = senate.count('R')

        d = 0
        r = 0

        senate = deque(senate)

        while D > 0 and R > 0:
            if senate[0] == 'D':
                if d < 0:
                    D -= 1
                    senate.popleft()
                else:
                    senate.append(senate.popleft())
                d += 1
                r -= 1
            else:
                if r < 0:
                    R -= 1
                    senate.popleft()
                else:
                    senate.append(senate.popleft())
                r += 1
                d -= 1
                
        return "Dire" if senate[0] == "D" else "Radiant"
# @lc code=end

