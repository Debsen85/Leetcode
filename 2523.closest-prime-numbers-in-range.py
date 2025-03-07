#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#

# @lc code=start
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True for number in range(right + 1)]

        sieve[0], sieve[1] = False, False

        for number in range(2, int(sqrt(right)) + 2):
            for value in range(2 * number, right + 1, number):
                sieve[value] = False

        answer = [-1, -1]
        minDifference = float("inf")

        l, r = None, left

        while r < (right + 1):
            if sieve[r]:
                if l and sieve[l]:
                    if r - l < minDifference:
                        if r - l <= 2:
                            return [l, r]
                        minDifference = r - l
                        answer = [l, r]
                l = r
            r += 1
        return answer
# @lc code=end

