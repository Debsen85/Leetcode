#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]

        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        total = prefixSum[-1]

        print(prefixSum, total)

        for i in range(1, len(prefixSum)):
            if prefixSum[i - 1] == total - prefixSum[i]:
                return (i - 1)
        
        return -1
# @lc code=end

