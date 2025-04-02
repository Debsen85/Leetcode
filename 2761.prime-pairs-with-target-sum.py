#
# @lc app=leetcode id=2761 lang=python3
#
# [2761] Prime Pairs With Target Sum
#

# @lc code=start
from math import sqrt
from typing import List

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        sieve = [True] * (n + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(sqrt(n)) + 1):
            for j in range(i + i, n + 1, i):
                sieve[j] = False
        answer = []
        for index in range(2, (n // 2) + 1):
            if sieve[index] and sieve[n - index]:
                answer.append((index, n - index))
        return answer
# @lc code=end

