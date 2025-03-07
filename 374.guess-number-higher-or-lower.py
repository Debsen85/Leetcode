#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n
        while L <= R:
            M = (L + R) // 2

            if guess(M) == -1:
                R = M - 1
            elif guess(M) == 1:
                L = M + 1
            else: 
                return M
# @lc code=end

