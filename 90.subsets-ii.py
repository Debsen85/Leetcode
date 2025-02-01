#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        def backtracking(i, currSet):
            if i == len(nums):
                answer.add(tuple(currSet[:]))
                return
            
            currSet.append(nums[i])
            backtracking(i + 1, currSet)
            currSet.pop()
            backtracking(i + 1, currSet)
        backtracking(0, [])
        return list(answer)
# @lc code=end

