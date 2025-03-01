#
# @lc app=leetcode id=1151 lang=python3
#
# [1151] Minimum Swaps to Group All 1's Together
#

# @lc code=start
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one = 0

        for d in data:
            if d:
                one += 1

        i, j = 0, 0
        answer = 10 ** 5

        c1 = 0
        c0 = 0

        while j < len(data):
            if data[j]:
                c1 += 1
            else:
                c0 += 1

            if j - i + 1 > one:
                if data[i]:
                    c1 -= 1
                else:
                    c0 -= 1
                i += 1
            
            if j - i + 1 == one:
                answer = min(answer, c0)

            j += 1
        return answer
# @lc code=end

