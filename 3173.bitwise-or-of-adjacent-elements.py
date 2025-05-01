#
# @lc app=leetcode id=3173 lang=python3
#
# [3173] Bitwise OR of Adjacent Elements
#

# @lc code=start
from typing import List

class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        answer = []
        for index in range(len(nums) - 1):
            answer.append(nums[index] | nums[index + 1])
        return answer
# @lc code=end

