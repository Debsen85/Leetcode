#
# @lc app=leetcode id=3411 lang=python3
#
# [3411] Maximum Subarray With Equal Products
#

# @lc code=start
from math import gcd, lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        answer = 0
        maximum = lcm(*nums) * max(nums)
        for i in range(len(nums)):
            product, Gcd, Lcm = 1, 0, 1
            for j in range(i, len(nums)):
                Gcd = gcd(nums[j], Gcd)
                Lcm = lcm(nums[j], Lcm)
                product *= nums[j]
                if product == Gcd * Lcm:
                    answer = max(answer, j - i + 1)
                if maximum < product:
                    break
        return answer
                

# @lc code=end

