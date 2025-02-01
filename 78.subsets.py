#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtracking(i, currSet):
            if i == len(nums):
                answer.append(currSet[:])
                return
            
            currSet.append(nums[i])
            backtracking(i + 1, currSet)
            currSet.pop()
            backtracking(i + 1, currSet)
        backtracking(0, [])
        return answer
# @lc code=end

