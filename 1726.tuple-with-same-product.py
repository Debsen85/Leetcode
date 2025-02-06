#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        productMap = defaultdict(int)
        total = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                productMap[nums[i] * nums[j]] += 1
        
        for product in productMap:
            number = productMap[product]
            total += (8 * ((number * (number - 1) // 2)))
        
        return total
        

# @lc code=end

