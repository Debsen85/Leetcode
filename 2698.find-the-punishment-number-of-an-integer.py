#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#

# @lc code=start
class Solution:
    def check(self, index, total, target, num):
        if index == len(num) and target == total:
            return True
        for j in range(index, len(num)):
            if self.check(j + 1, total + int(num[index : j + 1]), target, num):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        answer = 1
        for i in range(2, n + 1):
            if self.check(0, 0, i, str(i * i)):
                answer += (i * i)
        return answer
        
# @lc code=end

