#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        map = defaultdict(set)
        answer = 0

        for idea in ideas:
            map[idea[0]].add(idea[1:])

        for char in map:
            for rest in map:
                if char == rest:
                    continue
                intersect = 0
                for w in map[char]:
                    if w in map[rest]:
                        intersect += 1
                answer += (len(map[char]) - intersect) * (len(map[rest]) - intersect)
        
        return answer
        
# @lc code=end

