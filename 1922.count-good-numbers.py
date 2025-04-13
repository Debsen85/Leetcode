#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        h = n // 2
        m = 10 ** 9 + 7
        if n == 1: return 5
        if n % 2: return (pow(5, h, m) * pow(4, h, m) * 5) % m
        return (pow(5, h, m) * pow(4, h, m)) % m
# @lc code=end

