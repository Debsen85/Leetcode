#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        for key in hashMap:
            if hashMap[key] > (len(nums) // 2):
                return key
        return -1
# @lc code=end

