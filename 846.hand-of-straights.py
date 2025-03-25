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
        while numMap:
            prev = min(numMap.keys())
            for num in range(prev, prev + k):
                if num in numMap:
                    numMap[num] -= 1
                    if numMap[num] == 0:
                        numMap.pop(num)
                else:
                    return False 
        return True
# @lc code=end

