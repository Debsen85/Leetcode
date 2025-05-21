#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#

# @lc code=start
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mapping = {}
        answer = []
        for num in nums:
            if num in mapping:
                answer.append(num)
                if len(answer) == 2:
                    return answer
            mapping[num] = 1
        return []
# @lc code=end

