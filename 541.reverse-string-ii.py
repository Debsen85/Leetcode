#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        s = list(s)
        while index < len(s):
            i = index
            j = min(len(s), i + k) - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            index += 2 * k
        return "".join(s)
# @lc code=end

