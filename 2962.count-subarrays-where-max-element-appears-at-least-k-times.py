#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        number = max(nums)
        answer = 0
        mapHash = defaultdict(int)
        left, right = 0, 0
        while right < len(nums):
            mapHash[nums[right]] += 1
            while mapHash[number] == k:
                mapHash[nums[left]] -= 1
                left += 1
            answer += left
            right += 1
        return answer
# @lc code=end

