#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start
from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        answer = 0
        for index in range(n - 2):
            l, r = index + 1, n - 1
            while l < r:
                total = nums[index] + nums[l] + nums[r]
                if total < target:
                    answer += r - l
                    l += 1
                else:
                    r -= 1
        return answer
# @lc code=end

