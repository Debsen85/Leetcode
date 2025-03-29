#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#

# @lc code=start
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        for t in target:
            if t not in source:
                return -1
        n, m = len(source), len(target)
        p1, p2 = 0, 0
        answer = 0
        while p2 < m:
            p1 = 0
            while p1 < n and p2 < m:
                if source[p1] == target[p2]:
                    p2 += 1
                p1 += 1
            answer += 1
        return answer
# @lc code=end

