#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[nums[0]]]
        index = 1
        factorial = 2
        while index < len(nums):
            tempResult = []
            for i in range(len(result)):
                for j in range(factorial):
                    resultCopy = result[i].copy()
                    resultCopy.insert(j, nums[index])
                    tempResult.append(resultCopy)
            result = tempResult
            index += 1
            factorial += 1
        return result
# @lc code=end

