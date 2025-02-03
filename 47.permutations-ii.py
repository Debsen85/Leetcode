#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        nums.sort()
        for num in nums:
            result = []
            for ans in answer:
                for i in range(len(ans) + 1):
                    resultCopy = ans.copy()
                    resultCopy.insert(i, num)
                    if resultCopy not in result:
                        result.append(resultCopy)
            answer = result
        return answer
# @lc code=end

