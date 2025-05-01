#
# @lc app=leetcode id=2047 lang=python3
#
# [2047] Number of Valid Words in a Sentence
#

# @lc code=start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(s):
            hypen = 0
            for index, character in enumerate(s):
                if character.isdigit():
                    return False
                if character in ".,!":
                    if index != (len(s) - 1):
                        return False
                if character in "-":
                    hypen += 1
                    if hypen > 1:
                        return False
                    if index == 0 or index == (len(s) - 1):
                        return False
                    if not (s[index - 1].isalpha() and s[index + 1].isalpha()):
                        return False
            return True
        answer = 0
        for s in sentence.split():
            if valid(s):
                answer += 1
        return answer
# @lc code=end

