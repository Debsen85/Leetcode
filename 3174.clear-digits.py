#
# @lc app=leetcode id=3174 lang=python3
#
# [3174] Clear Digits
#

# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        answer = []
        for letter in s:
            if answer and letter.isdigit():
                answer.pop()
            else:
                answer.append(letter)
        return "".join(answer)
# @lc code=end

