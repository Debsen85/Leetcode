#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        L, R = 0, 0
        answer = 0
        wordMap = defaultdict(int)
        if k >= (n - 1):
            return n
        
        while R < n:
            wordMap[s[R]] += 1
            while (R - L + 1) - max(wordMap.values()) > k:
                wordMap[s[L]] -= 1
                L += 1
            answer = max(answer, R - L + 1)
            R += 1
        return answer 
# @lc code=end

