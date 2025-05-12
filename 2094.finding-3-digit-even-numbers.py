#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hashMap = {}
        answer = []
        for digit in digits:
            hashMap[digit] = hashMap.get(digit, 0) + 1
        for num in range(100, 999, 2):
            numMap = {}
            val = num
            while num:
                n = num % 10
                numMap[n] = numMap.get(n, 0) + 1
                num //= 10
            flag = True
            for key in numMap:
                if key not in hashMap or numMap[key] > hashMap[key]:
                    flag = False
                    break
            if flag:
                answer.append(val)
        return answer
# @lc code=end

