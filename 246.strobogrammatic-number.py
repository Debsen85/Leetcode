#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 1:
            if num in '018':
                return True
            return False
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] == '9':
                if num[r] != '6':
                    return False
            elif num[l] == '6':
                if num[r] != '9':
                    return False
            elif num[l] == '1':
                if num[r] != '1':
                    return False
            elif num[l] == '0':
                if num[r] != '0':
                    return False
            elif num[l] == '8':
                if num[r] != '8':
                    return False
            else:
                return False
            l += 1
            r -= 1
        if len(num) % 2:
            if num[len(num) // 2] in '018':
                return True
            return False
        return True
# @lc code=end

