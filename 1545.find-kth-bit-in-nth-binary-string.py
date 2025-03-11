#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        p = s
        for i in range(1, n + 1):
            s = p + '1' + ''.join('1' if v == '0' else '0' for v in p)[::-1]
            p = s
        return p[k - 1]
# @lc code=end

