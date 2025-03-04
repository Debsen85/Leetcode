#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        def check(n, r):
            if n == 3 and r == 0:
                return True
            if n <= 2 or r > 0:
                return False
            return check(n // 3, n % 3)
        return check(n, 0)
# @lc code=end

