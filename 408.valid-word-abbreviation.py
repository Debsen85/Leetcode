#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        numbers = []
        number, newAbbr = "", ""
        for s in abbr:
            if s.isdigit():
                if s == "0" and not len(number):
                    return False
                number += s
                if not newAbbr or newAbbr[-1] != "*":
                    newAbbr += "*"
            else:
                if len(number):
                    numbers.append(int(number))
                    number = ""
                newAbbr += s
        if len(number):
            numbers.append(int(number))
        i, j, k = 0, 0, 0
        while i < len(word) and j < len(newAbbr):
            if newAbbr[j].isalpha():
                if word[i] != newAbbr[j]: 
                    return False
                i += 1
                j += 1
            else:
                i += numbers[k]
                k += 1
                j += 1
        return (i == len(word) and j == len(newAbbr))
# @lc code=end

