#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 1:
            return False
        
        if k >= len(nums):
            k = len(nums) - 1

        current = set()

        for i in range(k + 1):
            if nums[i] in current:
                return True
            current.add(nums[i])

        i = 0
        j = k + 1

        while j < len(nums):
            current.remove(nums[i])

            if nums[j] in current:
                return True
            
            current.add(nums[j])

            i += 1
            j += 1
        
        return False
# @lc code=end

