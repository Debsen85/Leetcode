#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = ord(columnTitle[0]) - 65 + 1
        for letter in columnTitle[1:]:
            answer *= 26
            answer += ord(letter) - 65 + 1
        return answer 
# @lc code=end

