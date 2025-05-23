#
# @lc app=leetcode id=3032 lang=python3
#
# [3032] Count Numbers With Unique Digits II
#

# @lc code=start
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        answer = 0
        for num in range(a, b + 1):
            current = str(num)
            hashMap = {}
            flag = True
            for curr in current:
                if curr in hashMap:
                    flag = False
                    break
                hashMap[curr] = 1
            if flag:
                answer += 1
        return answer
# @lc code=end

