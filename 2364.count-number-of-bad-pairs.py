#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairMap = defaultdict(int)
        for i, num in enumerate(nums):
            pairMap[num - i] += 1
        length = len(nums)
        answer = (length * (length - 1)) // 2
        for key in pairMap:
            if pairMap[key] > 1:
                answer -= (pairMap[key] * (pairMap[key] - 1)) // 2
        return answer
# @lc code=end

