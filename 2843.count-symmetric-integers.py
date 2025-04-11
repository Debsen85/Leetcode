#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for num in range(low, high + 1):
            if len(str(num)) % 2:
                continue
            num = str(num)
            l, r = 0, len(num) - 1
            s1, s2 = 0, 0
            while l < r:
                s1 += int(num[l])
                s2 += int(num[r])
                l += 1
                r -= 1
            if s1 == s2:
                answer += 1
        return answer 
# @lc code=end

