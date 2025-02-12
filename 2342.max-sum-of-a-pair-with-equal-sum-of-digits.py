#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def findSum(self, num):
        total = 0
        while num:
            total += (num % 10)
            num //= 10
        return total
    
    def maximumSum(self, nums: List[int]) -> int:
        hashMap = defaultdict(deque)
        answer = 0
        for num in nums:
            total = self.findSum(num)
            if total in hashMap:
                if len(hashMap[total]) < 2:
                    if hashMap[total][0] > num:
                        hashMap[total].appendleft(num)
                    else:
                        hashMap[total].append(num)
                else:
                    if hashMap[total][1] < num:
                        hashMap[total].append(num)
                        hashMap[total].popleft()
                    elif hashMap[total][0] < num <= hashMap[total][1]:
                        hashMap[total].popleft()
                        hashMap[total].appendleft(num)
                answer = max(answer, hashMap[total][0] + hashMap[total][1])
            else:
                hashMap[total].append(num)
        return answer if answer else -1
# @lc code=end

