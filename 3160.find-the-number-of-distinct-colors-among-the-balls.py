#
# @lc app=leetcode id=3160 lang=python3
#
# [3160] Find the Number of Distinct Colors Among the Balls
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        answer = []
        total = 0
        colours = {}
        balls = {}
        for ball, colour in queries:
            if ball not in balls:
                balls[ball] = colour
            else:
                colours[balls[ball]] -= 1
                if colours[balls[ball]] == 0:
                    total -= 1
                balls[ball] = colour
            if colour not in colours:
                colours[colour] =  1
                total += 1
            else:
                colours[colour] += 1
                if colours[colour] == 1:
                    total += 1
            answer.append(total)
        return answer
# @lc code=end

