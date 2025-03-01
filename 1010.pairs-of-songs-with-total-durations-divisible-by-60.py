#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timeMap = {}
        for t in time:
            key = t % 60
            timeMap[key] = timeMap.get(key, 0) + 1
        
        answer = 0

        for key in timeMap:
            if (60 - key) % 60 in timeMap:
                if (60 - key) % 60 == key:
                    answer += (timeMap[key] * (timeMap[key] - 1)) // 2
                else:
                    answer += (timeMap[key] * timeMap[(60 - key) % 60]) 
                    timeMap[(60 - key) % 60] = 0

        return answer
# @lc code=end

