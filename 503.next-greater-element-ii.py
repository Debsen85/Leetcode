#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-(10 ** 9 + 1)] * len(nums)
        stack = []

        for i in reversed(range(len(nums))):
            if stack: 
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if stack:
                    answer[i] = stack[-1]

            stack.append(nums[i])
        i = len(nums) - 1
        print(*answer)

        while stack and stack[0] > nums[i]:
            if answer[i] == -(10 ** 9 + 1):
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if stack:
                    answer[i] = stack[-1]
            i -= 1

        for i in range(len(answer)):
            if answer[i] == -(10 ** 9 + 1):
                answer[i] = -1

        return answer
# @lc code=end

