#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k

        answer = 0
        total = arr[0]

        L, R = 0, 1

        while R < len(arr):

            if R - L == k and target <= total:
                answer += 1

            if R - L + 1 > k:
                total -= arr[L]
                L += 1

            total += arr[R]
            R += 1

        if target <= total:
            answer += 1   
            
        return answer
            

# @lc code=end

