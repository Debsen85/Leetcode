#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        for key in hashMap:
            if hashMap[key] % 2 == 1:
                return False
        return True
# @lc code=end

