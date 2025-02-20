#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        nums = set(nums)

        def backtracking(size, current):
            if length == size:
                binString = "".join(current)
                if binString not in nums:
                    return binString
                return ""

            for string in "01":
                current.append(string)
                binString = backtracking(size + 1, current)
                if binString:
                    return binString
                current.pop()
            
            return ""
        
        return backtracking(0, [])
# @lc code=end

