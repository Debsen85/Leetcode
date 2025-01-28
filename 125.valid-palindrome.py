#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        
        L, R = 0, len(string) - 1

        while L < R:
            if string[L] != string[R]:
                return False
            L += 1
            R -= 1
        
        return True
        
# @lc code=end

