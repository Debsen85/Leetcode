#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = [[heights[length - 1], length - 1]]
        answer = heights[length - 1]
        i = length - 2
        while i >= 0:
            answer = max(answer, heights[i])
            if heights[i] > stack[-1][0]:
                j = len(stack) - 1
                while j >= 0:
                    answer = max(answer, (stack[j][1] - i + 1) * stack[j][0])
                    j -= 1
                stack.append([heights[i], i])
            else:
                position = i
                while stack and stack[-1][0] >= heights[i]:
                    value = stack.pop()
                    answer = max(answer, (value[1] - i + 1) * heights[i])
                    position = value[1]
                j = len(stack) - 1
                while stack and j >= 0:
                    answer = max(answer, (stack[j][1] - i + 1) * min(stack[j][0], heights[i]))
                    j -= 1
                stack.append([heights[i], position])
            i -= 1
        return answer
            
        
# @lc code=end

