#
# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powerOfTwo = []
        numberMap = defaultdict(int)
        mod = 10 ** 9 + 7
        answer = 0

        for power in range(22):
            powerOfTwo.append(2 ** power)
        for number in deliciousness:
            numberMap[number] += 1

        for key in numberMap:
            for check in powerOfTwo:
                value = check - key
                if value in numberMap:
                    if value == key:
                        answer += (((numberMap[key] - 1) * numberMap[key]) // 2) % mod
                    else:
                        answer += (numberMap[key] * numberMap[value]) % mod
            numberMap[key] = 0
        return answer
# @lc code=end

