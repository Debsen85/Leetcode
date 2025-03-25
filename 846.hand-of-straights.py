#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from typing import Counter, List

class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        numMap = Counter(nums)
        nums.sort()

        for num in nums:
            if numMap[num] == 0:
                continue
            howMany = numMap[num]
            numMap[num] = 0
            for val in range(num + 1, num + k):
                if val in numMap and numMap[val] >= howMany:
                    numMap[val] -= howMany
                else:
                    return False
        return True
# @lc code=end

