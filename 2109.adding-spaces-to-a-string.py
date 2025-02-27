#
# @lc app=leetcode id=2109 lang=python3
#
# [2109] Adding Spaces to a String
#

# @lc code=start
from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = []
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                answer.append(" ")
                j += 1
            answer += s[i]
        if j == len(spaces) - 1:
            answer.append(s[i])
        return "".join(answer)

# @lc code=end

