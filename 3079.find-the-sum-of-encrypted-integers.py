#
# @lc app=leetcode id=3079 lang=python3
#
# [3079] Find the Sum of Encrypted Integers
#

# @lc code=start
from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        stringList = [list(str(num)) for num in nums]
        answer = 0
        for string in stringList:
            maxValue = string[0]
            for letter in string[1 : ]:
                maxValue = max(maxValue, letter)
            answer += int(maxValue * len(string)) 
        return answer
# @lc code=end

