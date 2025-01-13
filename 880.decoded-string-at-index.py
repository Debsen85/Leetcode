#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        i = 0
        length = 0
        while i < len(s):
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1
        i = len(s) - 1
        while i >= 0:
            k %= length
            if s[i].isalpha():
                if k == 0:
                    return s[i]
                else:
                    length -= 1
            else:
                length //= int(s[i])
            i -= 1
        return ""
# @lc code=end

