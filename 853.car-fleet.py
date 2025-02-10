#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        for p, s in zip(position, speed):
            time[p] = (float((float(target) - float(p)) / float(s)))
        stack = []
        answer = 1
        time = dict(sorted(time.items(), reverse = True))
        for key in time:
            if stack and stack[-1] < time[key]:
                stack.append(time[key])
                answer += 1
            else:
                if not stack:
                    stack.append(time[key])
        return answer
# @lc code=end

