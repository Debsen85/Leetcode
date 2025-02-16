#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        i, j = 0, 0
        maxLength = 0
        for j, letter in enumerate(s):
            hashMap[letter] += 1
            while i < len(s) and hashMap[letter] > 2:
                hashMap[s[i]] -= 1
                i += 1
            maxLength = max(maxLength, j - i + 1)
        return maxLength
        
# @lc code=end

