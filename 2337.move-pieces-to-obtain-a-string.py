#
# @lc app=leetcode id=2337 lang=python3
#
# [2337] Move Pieces to Obtain a String
#

# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        r = 0
        j = len(target) - 1
        while j > -1:
            if target[j] == 'R':
                r += 1
            if start[j] == 'R':
                if r > 0:
                    r -= 1
                else:
                    return False
            j -= 1
        
        i = 0
        l = 0
        while i < len(target) - 1:
            if target[i] == 'L':
                l += 1
            if start[i] == 'L':
                if l > 0:
                    l -= 1
                else:
                    return False
            i += 1
        
        s, t = "", ""
        for w1, w2 in zip(start, target):
            s += w1 if w1 in 'LR' else ''
            t += w2 if w2 in 'LR' else ''
            
        return s == t
# @lc code=end

