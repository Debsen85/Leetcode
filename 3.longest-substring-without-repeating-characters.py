#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R, n = 0, 0, len(s)
        answer = 0
        hashSet = set()
        while R < n:
            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1
            hashSet.add(s[R])
            answer = max(answer, R - L + 1)
            R += 1
        return answer

# @lc code=end

