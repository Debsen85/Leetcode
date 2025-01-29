#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = {}
        mapS2 = {}
        have, need, k = 0, 0, len(s1)
        for s in s1:
            mapS1[s] = mapS1.get(s, 0) + 1
        need = len(mapS1)
        L, R = 0, 0
        while R < len(s2):
            mapS2[s2[R]] = mapS2.get(s2[R], 0) + 1
            if mapS2[s2[R]] == mapS1.get(s2[R], 0):
                have += 1
            if have == need:
                return True
            if R - L + 1 == k:
                if mapS2[s2[L]] == mapS1.get(s2[L], 0):
                    have -= 1
                mapS2[s2[L]] -= 1
                L += 1
            R += 1
        return False

# @lc code=end

