#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = 0
        odd = 0
        even = 1 # Zero is even

        for num in arr:
            prefixSum += num
            if prefixSum % 2:
                odd += 1
            else:
                even += 1

        return (odd * even) % (10 ** 9 + 7)
# @lc code=end

