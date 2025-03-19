#
# @lc app=leetcode id=1426 lang=python3
#
# [1426] Counting Elements
#

# @lc code=start
from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        check = set(arr)
        answer = 0
        for num in arr:
            if num + 1 in check:
                answer += 1
        return answer
# @lc code=end

