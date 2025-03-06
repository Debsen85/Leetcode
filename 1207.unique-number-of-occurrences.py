#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = defaultdict(int)

        for a in arr:
            hashMap[a] += 1

        v = hashMap.values()

        return len(v) == len(set(v))
# @lc code=end

