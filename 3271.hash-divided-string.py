#
# @lc app=leetcode id=3271 lang=python3
#
# [3271] Hash Divided String
#

# @lc code=start
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        newString = ""
        index = 0
        while index < len(s):
            newChar = 0
            for i in range(index, min(len(s), index + k)):
                newChar += (ord(s[i]) - 97)
            newString += chr(97 + (newChar % 26))
            index += k
        return newString
# @lc code=end

