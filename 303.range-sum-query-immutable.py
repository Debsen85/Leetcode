#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[i - 1] + nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - (self.prefix[left - 1 ] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

