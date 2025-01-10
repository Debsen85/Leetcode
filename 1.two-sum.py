#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from collections import defaultdict
from typing import Counter, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            reminder = target - num
            if reminder in d and i != d[reminder]:
                return [i, d[reminder]]

# @lc code=end
