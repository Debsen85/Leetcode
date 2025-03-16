#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        wordMap = defaultdict(int)
        for letter in s:
            wordMap[letter] += 1
        if len(s) % 2:
            odd, even = 0, 0
            for key in wordMap:
                if wordMap[key] % 2:
                    odd += 1
                else:
                    even += 1
                if odd > 1:
                    return False
        else:
            for key in wordMap:
                if wordMap[key] % 2:
                    return False
        return True
# @lc code=end

