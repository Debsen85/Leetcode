#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#

# @lc code=start
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = 'aeiou'
        prefix = [0]
        for word in words:
            add = 0
            if word[0] in vowel and word[-1] in vowel:
                add = 1
            prefix.append(prefix[-1] + add)
        answer = []
        for l, r in queries:
            answer.append(prefix[r + 1] - prefix[l])
        return answer
# @lc code=end

