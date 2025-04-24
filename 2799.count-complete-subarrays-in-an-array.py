#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        answer = 0
        l, r = 0, 0
        hashMap = defaultdict(int)
        while r < len(nums):
            hashMap[nums[r]] += 1
            while len(hashMap) >= total:
                hashMap[nums[l]] -= 1
                if hashMap[nums[l]] == 0:
                    hashMap.pop(nums[l])
                l += 1
                answer += len(nums) - r
            r += 1
        return answer
# @lc code=end

