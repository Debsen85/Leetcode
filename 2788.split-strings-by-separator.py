#
# @lc app=leetcode id=2788 lang=python3
#
# [2788] Split Strings by Separator
#

# @lc code=start
from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            answer.extend(word.split(separator))
        return [ans for ans in answer if len(ans) > 0]
# @lc code=end

