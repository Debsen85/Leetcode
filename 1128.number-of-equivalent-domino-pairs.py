#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashMap = defaultdict(int)
        for a, b in dominoes:
            if  a > b:
                a, b = b, a
            hashMap[a * 10 + b] += 1
        answer = 0
        for value in hashMap:
            val = hashMap[value]
            answer += (val * (val - 1)) // 2
        return answer
    
# @lc code=end

