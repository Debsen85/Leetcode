#
# @lc app=leetcode id=2595 lang=python3
#
# [2595] Number of Even and Odd Bits
#

# @lc code=start
from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        answer = [0, 0]
        binaryString = bin(n)[2 : ][::-1]
        for index in range(len(binaryString)):
            if binaryString[index] == '1':
                answer[index % 2] += 1
        return answer
# @lc code=end

