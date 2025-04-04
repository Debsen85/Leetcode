#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#

# @lc code=start
class Solution:
    def removeVowels(self, s: str) -> str:
        answer = []
        vowels = "aeiou"
        for s in string: # type: ignore
            if s not in vowels:
                answer.append(s)
        return "".join(answer)
# @lc code=end

