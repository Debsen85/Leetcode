#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber:
            answer = str(chr(65 + ((columnNumber - 1)% 26))) + answer
            columnNumber = (columnNumber - 1) // 26
        return answer
# @lc code=end

