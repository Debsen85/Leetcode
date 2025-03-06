#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for word in word1:
            map1[word] += 1
        
        for word in word2:
            map2[word] += 1

        for key in map1:
            if key not in map2:
                return False
        
        for key in map2:
            if key not in map1:
                return False
            
        return sorted(map1.values()) == sorted(map2.values())
# @lc code=end

