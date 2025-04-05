#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def generateSubsets(index, subset):
            if index == len(nums):
                subsets.append(subset[:])
                return
            generateSubsets(index + 1, subset)
            subset.append(nums[index])
            generateSubsets(index + 1, subset)
            subset.pop()
        generateSubsets(0, [])
        answer = 0
        for subset in subsets:
            xor = 0
            for num in subset:
                xor ^= num
            answer += xor
        return answer
# @lc code=end

