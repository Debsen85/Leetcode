#
# @lc app=leetcode id=1100 lang=python3
#
# [1100] Find K-Length Substrings With No Repeated Characters
#

# @lc code=start
from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        i, j = 0, 0
        letterMap = defaultdict(int)
        unique = 0
        answer = 0

        while j < len(s):
            letterMap[s[j]] += 1

            if letterMap[s[j]] == 1:
                unique += 1
            
            if j - i + 1 > k:
                letterMap[s[i]] -= 1
                if letterMap[s[i]] == 0:
                    unique -= 1
                i += 1
            
            if j - i + 1 == k and unique == k:
                answer += 1
            j += 1

        return answer
# @lc code=end

