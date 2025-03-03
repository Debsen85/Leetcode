#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        alphabetMap = defaultdict(int)

        for letter in s:
            alphabetMap[letter] += 1

        answer = 0

        for key in alphabetMap:
            if alphabetMap[key] <= 2:
                answer += alphabetMap[key]
            else:
                if alphabetMap[key] % 2:
                    answer += 1
                else:
                    answer += 2
        
        return answer
# @lc code=end

