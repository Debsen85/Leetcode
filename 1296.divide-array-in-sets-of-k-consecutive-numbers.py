#
# @lc app=leetcode id=1296 lang=python3
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#

# @lc code=start
from typing import Counter, List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        numMap = Counter(nums)
        nums.sort()

        for num in nums:
            if numMap[num] == 0:
                continue
            numMap[num] -= 1
            for val in range(num + 1, num + k):
                if val in numMap and numMap[val]:
                    numMap[val] -= 1
                else:
                    return False
        return True
# @lc code=end

