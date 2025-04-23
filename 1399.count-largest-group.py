#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
from collections import defaultdict

class Solution:
    def digitSum(self, num):
        answer = 0
        while num:
            answer += num % 10
            num //= 10
        return answer

    def countLargestGroup(self, n: int) -> int:
        hashMap = defaultdict(list)
        for num in range(1, n + 1):
            hashMap[self.digitSum(num)].append(num)
        highest, answer = 0, 0
        for num in hashMap:
            if len(hashMap[num]) > highest:
                highest = len(hashMap[num])
                answer = 1
            elif len(hashMap[num]) == highest:
                answer += 1
        return answer
        
# @lc code=end

