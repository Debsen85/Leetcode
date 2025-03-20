#
# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = []

        while n != 0:
            n, r = n // (-2), n % (-2)

            if r < 0:
                n, r = n + 1, r + 2

            result.append(str(r))

        return "".join(result[::-1])
# @lc code=end

