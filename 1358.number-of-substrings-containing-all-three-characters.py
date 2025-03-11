#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashMap = defaultdict(int)
        i, j, result = 0, 0, 0
        while j < len(s):
            hashMap[s[j]] += 1

            while len(hashMap) == 3:
                result += len(s) - j
                hashMap[s[i]] -= 1
                if hashMap[s[i]] == 0:
                    hashMap.pop(s[i])
                i += 1

            j += 1
        return result

        # @lc code=end

