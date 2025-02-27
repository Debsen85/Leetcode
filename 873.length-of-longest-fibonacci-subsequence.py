#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr.sort()
        arrMap = {}

        for i, num in enumerate(arr):
            arrMap[num] = i
        
        answer = 0
        current = 2
        i = 0

        while i < (len(arr) - 2):
            l = i
            r = i + 1
            j = i + 1
            current = 2
            while r < (len(arr) - 1):
                add = arr[l] + arr[r]

                if add in arrMap:
                    current += 1
                    l = r
                    r = arrMap[add]

                else:
                    l = i
                    r = j + 1
                    j += 1
                    current = 2

                answer = max(answer, current)
            i += 1
        return answer if answer > 2 else 0

        
# @lc code=end

